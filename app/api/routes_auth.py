from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserLogin, TokenRefresh
from app.models.user import User
from app.core.security import get_password_hash, verify_password
from app.core.jwt import create_access_token, create_refresh_token, decode_token
from app.api.deps import oauth2_scheme, token_blacklist
from fastapi.security import HTTPAuthorizationCredentials

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(name=user.name, email=user.email, hashed_password=get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    return {"msg": "User registered"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.email})
    refresh_token = create_refresh_token({"sub": db_user.email})
    return {"access_token": access_token, "refresh_token": refresh_token}

@router.post("/logout")
def logout(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    token_blacklist.add(credentials.credentials)
    return {"msg": "Logged out successfully"}

@router.post("/refresh")
def refresh(data: TokenRefresh):
    try:
        payload = decode_token(data.refresh_token)
        return {"access_token": create_access_token({"sub": payload.get("sub")})}
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")