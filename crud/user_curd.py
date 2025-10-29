from sqlalchemy.orm import Session
from model.user_model import UserModel
from schemas.users_schemas import UserCreateSchema, UserUpdateSchema
from datetime import datetime

def get_all_users_operation(db: Session):
    return db.query(UserModel).all()

def get_user_by_email_operation(db: Session, u_email:str):
    return  db.query(UserModel).filter(UserModel.u_email == u_email).first()

def create_user_operation(db:Session, userCreate:UserCreateSchema):
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

def update_user_operation(db: Session, u_email:str, userUpdate:UserUpdateSchema):
    db_user = db.query(UserModel).filter(UserModel.u_email == u_email).first()
    if not db_user:
        return None

    mapping = {
        "name": "u_name",
        "email": "u_email",
        "mobile": "u_mobile_number",
        "age": "u_age",
        "gender": "u_gender"
    }

    update_data = userUpdate.model_dump(exclude_unset=True,by_alias=True)
    print("Update data:", update_data)
    for key, value in update_data.items():
        setattr(db_user, mapping[key], value)

    db_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    print("After commit:", db_user.u_name)
    return db_user


