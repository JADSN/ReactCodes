
# from dependencies import Session, Depends, HTTPException, status, get_db, oauth2_scheme
# from tokenizer import TokenData, SECRET_KEY, ALGORITHM

# from hasher import verify_password

# from jose import jwt, JWTError

# from repositories.user import read_first_user


# def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
#     user_auth = read_first_user(username, db)
#     if not user_auth:
#         return False
#     if not verify_password(password, user_auth.password):
#         return False
#     return user_auth


# def validate_auth(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#         token_data = TokenData(email=email)
#     except JWTError:
#         raise credentials_exception
#     user_email = read_first_user(token_data.email, db)

#     if user_email is None:
#         raise credentials_exception
#     return user_email
