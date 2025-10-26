from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from crud import user
from schemas import users_schemas
from model.user_model import UserModel

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[users_schemas.UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)


@router.get("/{email}", response_model=users_schemas.UserResponseSchema)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = user.get_user_by_email(db, email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return db_user


@router.post("/", response_model=users_schemas.UserResponseSchema)
def create_user_route(new_user: users_schemas.UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.u_email == new_user.u_email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        return user.create_user(db, new_user)

@router.patch("/{email}", response_model=users_schemas.UserResponseSchema)
def update_user_route(email: str, user_update: users_schemas.UserUpdateSchema, db: Session = Depends(get_db)):
    update_user = user.update_user(db, email, user_update)
    if not update_user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user
