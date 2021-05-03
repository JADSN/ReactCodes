# from datetime import datetime, timezone

# from dependencies import Session, Depends, get_db, APIRouter, oauth2_scheme

# from schemas import UserItem

# # from repositories import user
# from auth import validate_auth

# from repositories import user


# router = APIRouter(
#     prefix="/users",
#     tags=["users"]
# )


# @router.get("/", status_code=200)
# async def read_one(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     return validate_auth(token, db)


# @router.post("/", status_code=200)
# async def create(req_body: UserItem, db: Session = Depends(get_db)):
#     return user.create(req_body, db)
