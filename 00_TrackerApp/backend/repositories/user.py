# from datetime import datetime, timezone

# from schemas import UserItem
# from models import UserItem

# from dependencies import Session, Depends, HTTPException, status, get_db, oauth2_scheme
# from tokenizer import TokenData, SECRET_KEY, ALGORITHM

# from hasher import hash_password

# from jose import jwt, JWTError


# def read_first_user(email: str, db: Session = Depends(get_db)):
#     item = db.query(UserItem).where(UserItem.email == email)

#     if not item.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Item with id {id} not found")

#     db.commit()

#     user = item.first()
#     return UserItem(email=user.email, password=user.password)


# def create(req_body: UserItem, db: Session = Depends(get_db)):

#     hashed_password = hash_password(req_body.password)

#     new_data = UserItem(
#         email=req_body.email, password=hashed_password)

#     db.add(new_data)
#     db.commit()
#     db.refresh(new_data)
#     return new_data
