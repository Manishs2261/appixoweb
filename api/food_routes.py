from typing import List, Optional

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Query
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


@router.get("/search", response_model= List[food_schemas.FoodResponseSchema])
def search_food(db: Session = Depends(get_db),
                food_name : Optional[str] = Query(None),
                city : Optional[str] = Query(None),
                state : Optional[str] = Query(None),
                address : Optional[str] = Query(None),
                F_type : Optional[str] = Query(None),
                ):
    result = food_curd.search_food_operation(
        db=db,
        name=food_name,
        type=F_type,
        address= address,
        city= city,
        state= state,
    )

    return  result


@router.delete("/{foodId", response_model=food_schemas.FoodResponseSchema)
def delete_food(foodId:int, db: Session = Depends(get_db)):
    result = food_curd.delete_food_operation(db, foodId)
    if not result:
        raise HTTPException(status_code=404, detail="Food not found")

    return result
