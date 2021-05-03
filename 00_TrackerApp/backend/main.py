# from repositories.user import read_first_user
from datetime import timedelta

# Uvicorn
import uvicorn

# FastApi imports
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Database imports
from database import engine, Base, get_db

# Routes imports
from routers import tasks, users, auth

# Token
from tokenizer import Token, create_access_token

# Sqlalchemy
from sqlalchemy.orm import Session

# Schemas
# from schemas import UserItem

# Hash
from hasher import verify_password, hash_password

# Auth
# from auth import authenticate_user

# Application instance
app = FastAPI()

# to get a string like this run:
# openssl rand -hex 32

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database configuration
Base.metadata.create_all(engine)

# Mount of routes
# app.include_router(users.router)
app.include_router(tasks.router)
# app.include_router(auth.router)


@app.get("/")
async def root():
    return {"Hello": "World"}


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     ACCESS_TOKEN_EXPIRE_MINUTES = 30

#     user = authenticate_user(
#         form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
