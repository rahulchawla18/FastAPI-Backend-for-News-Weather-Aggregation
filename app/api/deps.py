from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from app.core.config import settings
import time
from collections import defaultdict

oauth2_scheme = HTTPBearer()
token_blacklist = set()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    token = credentials.credentials
    if token in token_blacklist:
        raise HTTPException(status_code=401, detail="Token blacklisted")
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")  # or return token if needed
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# In-memory IP-based rate limiting
RATE_LIMIT = 5
TIME_WINDOW = 60
request_log = defaultdict(list)

def rate_limiter(request: Request):
    ip = request.client.host
    now = time.time()
    request_log[ip] = [t for t in request_log[ip] if t > now - TIME_WINDOW]
    if len(request_log[ip]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    request_log[ip].append(now)
