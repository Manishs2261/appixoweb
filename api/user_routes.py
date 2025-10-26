from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import  Session

from core.database import get_db
from crud import user
from schemas import users_schemas

router =APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model = list[users_schemas.UserSchema])
def get_all_users(db:Session = Depends(get_db)):
    return user.get_all_users(db)

@router.get("/{email}", response_model=users_schemas.UserSchema)
def get_user_by_email(email:str, db:Session = Depends(get_db)):

    db_user = user.get_user_by_email(db,email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return db_user
