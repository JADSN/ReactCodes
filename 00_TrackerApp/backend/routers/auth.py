# from datetime import datetime, timezone

# from dependencies import Session, Depends, get_db, APIRouter, oauth2_scheme

# from auth import validate_auth

# router = APIRouter(
#     prefix="/auth",
#     tags=["auth"]
# )


# @router.get("/", status_code=200)
# async def auth(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     return validate_auth(token, db)
