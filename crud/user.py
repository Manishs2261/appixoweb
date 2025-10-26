from sqlalchemy.orm import Session
from model.user_model import UserModel
from schemas.users_schemas import UserCreateSchema

def get_all_users(db: Session):
    return db.query(UserModel).all()

def get_user_by_email(db: Session,u_email:str):
    return  db.query(UserModel).filter(UserModel.u_email == u_email).first()

def create_user(db:Session, userCreate:UserCreateSchema ):
    db_user = UserModel(
        u_name=userCreate.u_name,
        u_email=userCreate.u_email,
        u_mobile_number=userCreate.u_mobile_number,
        u_age=userCreate.u_age,
        u_gender=userCreate.u_gender,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user