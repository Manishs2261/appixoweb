from sqlalchemy.orm import Session
from model.user_model import UserModel

def get_all_users(db: Session):
    return db.query(UserModel).all()

def get_user_by_email(db: Session,u_email:str):
    return  db.query(UserModel).filter(UserModel.u_email == u_email).first()