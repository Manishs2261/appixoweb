from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas import food_schemas
from model.food_model import FoodModel
from crud import food_curd

router = APIRouter(prefix="/food", tags=["Foods"])


@router.get("/", response_model=List[food_schemas.FoodResponseSchema])
def get_all_food(db: Session = Depends(get_db)):
    return food_curd.get_all_food_operation(db)


@router.post("", response_model=food_schemas.FoodResponseSchema)
def create_food_operation(food: food_schemas.FoodCreateSchema, db: Session = Depends(get_db)):
    return food_curd.create_food_operation(db, food)

@router.patch("/{foodId", response_model=food_schemas.FoodResponseSchema)
def update_food(foodId:int,food_update:food_schemas.FoodUpdateSchema,db: Session = Depends(get_db)):
    update_data = food_curd.update_food_operation(db, foodId, food_update)

    if not update_food:
        raise HTTPException(status_code=404, detail="Food not found")

    return update_data
