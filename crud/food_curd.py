from fastapi import HTTPException
from sqlalchemy.orm import Session

from model.food_model import FoodModel
from schemas.food_schemas import FoodCreateSchema, FoodUpdateSchema
from datetime import datetime


def get_all_food_operation(db: Session):
    return db.query(FoodModel).all()


def create_food_operation(db: Session, foodCreate: FoodCreateSchema):
    try:
        new_food = FoodModel(
            u_id=1,
            f_name=foodCreate.f_name,
            f_description=foodCreate.f_description,
            f_type=foodCreate.f_type,
            f_address=foodCreate.f_address,
            f_landmark=foodCreate.f_landmark,
            f_city=foodCreate.f_city,
            f_state=foodCreate.f_state,
            f_latitude=foodCreate.f_latitude,
            f_longitude=foodCreate.f_longitude,
            f_mobile_number=foodCreate.f_mobile_number,
            f_breakfast_cost=foodCreate.f_breakfast_cost,
            f_lunch_or_dinner_cost=foodCreate.f_lunch_or_dinner_cost,
            f_breakfast_and_lunch_or_dinner_cost=foodCreate.f_breakfast_and_lunch_or_dinner_cost,
            f_lunch_and_dinner_cost=foodCreate.f_lunch_and_dinner_cost,
            f_thali_cost=foodCreate.f_thali_cost,
            f_cup_of_rice=foodCreate.f_cup_of_rice,
            f_dal=foodCreate.f_dal,
            f_roti=foodCreate.f_roti,
            f_sabji=foodCreate.f_sabji,
            f_food_category=foodCreate.f_food_category,
            # JSON fields
            f_daily_item=foodCreate.f_daily_item,
            f_restructure_menu=foodCreate.f_restructure_menu,
            f_subscription=foodCreate.f_subscription,
            f_faq=foodCreate.f_faq,
            f_mess_rules=foodCreate.f_mess_rules,
            f_report=foodCreate.f_report,
            f_image_list=foodCreate.f_image_list,
            # timestamps
            atCreate=datetime.utcnow(),
            atUpdate=datetime.utcnow()
        )

        db.add(new_food)
        db.commit()
        db.refresh(new_food)
        return new_food

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


def update_food_operation(db: Session, f_id: int, foodUpdate: FoodUpdateSchema):
    db_food = db.query(FoodModel).filter(FoodModel.f_id == f_id).first()
    if not db_food:
        raise HTTPException(status_code=404, detail="Food not found")

    food_data = foodUpdate.model_dump(exclude_unset=True)
    for key, value in food_data.items():
        setattr(db_food, key, value)

    db.commit()
    db.refresh(db_food)
    return db_food


def search_food_operation(db: Session,
                          name: str = None,
                          type: str = None,
                          address: str = None,
                          city: str = None,
                          state: str = None,
                          ):
    query = db.query(FoodModel)

    if name:
        query = query.filter(FoodModel.f_name.ilike(f"%{name}%"))
    if type:
        query = query.filter(FoodModel.f_type.ilike(f"%{type}%"))
    if address:
        query = query.filter(FoodModel.f_address.ilike(f"%{address}%"))
    if city:
        query = query.filter(FoodModel.f_address.ilike(f"%{city}%"))
    if state:
        query = query.filter(FoodModel.f_address.ilike(f"%{state}%"))

    return  query.all()

def delete_food_operation(db:Session, f_id: int):
    db_food = db.query(FoodModel).filter(FoodModel.f_id == f_id).first()

    if not db_food:
         raise HTTPException(status_code=404, detail="Food not found")

    db.delete(db_food)
    db.commit()
    return db_food



