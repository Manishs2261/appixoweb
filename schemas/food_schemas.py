from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime

class FoodCreateSchema(BaseModel):
    f_name: str = Field(..., alias="name")
    f_description: Optional[str] = Field(None, alias="description")
    f_type: Optional[str] = Field(None, alias="type")
    f_address: Optional[str] = Field(None, alias="address")
    f_landmark: Optional[str] = Field(None, alias="landmark")
    f_city: Optional[str] = Field(None, alias="city")
    f_state: Optional[str] = Field(None, alias="state")
    f_latitude: Optional[float] = Field(None, alias="latitude")
    f_longitude: Optional[float] = Field(None, alias="longitude")

    f_mobile_number: Optional[str] = Field(None, alias="mobile_number")

    f_breakfast_cost: Optional[float] = Field(None, alias="breakfast_cost")
    f_lunch_or_dinner_cost: Optional[float] = Field(None, alias="lunch_or_dinner_cost")
    f_breakfast_and_lunch_or_dinner_cost: Optional[float] = Field(None, alias="breakfast_and_lunch_or_dinner_cost")
    f_lunch_and_dinner_cost: Optional[float] = Field(None, alias="lunch_and_dinner_cost")
    f_thali_cost: Optional[float] = Field(None, alias="thali_cost")
    f_cup_of_rice: Optional[float] = Field(None, alias="cup_of_rice")

    f_dal: Optional[str] = Field(None, alias="dal")
    f_roti: Optional[str] = Field(None, alias="roti")
    f_sabji: Optional[str] = Field(None, alias="sabji")
    f_food_category: Optional[str] = Field(None, alias="food_category")

    f_daily_item: Optional[Any] = Field(None, alias="daily_item")
    f_restructure_menu: Optional[Any] = Field(None, alias="restructure_menu")
    f_subscription: Optional[Any] = Field(None, alias="subscription")
    f_faq: Optional[Any] = Field(None, alias="faq")
    f_mess_rules: Optional[Any] = Field(None, alias="mess_rules")
    f_report: Optional[Any] = Field(None, alias="report")
    f_image_list: Optional[Any] = Field(None, alias="image_list")

    f_disable: bool = Field(False, alias="is_disabled")
    f_isDelete: bool = Field(False, alias="is_deleted")

    u_id: Optional[int] = Field(None, alias="user_id")

    class Config:
        populate_by_name = True



class FoodUpdateSchema(BaseModel):
    f_name: Optional[str] = Field(None, alias="name")
    f_description: Optional[str] = Field(None, alias="description")
    f_type: Optional[str] = Field(None, alias="type")
    f_address: Optional[str] = Field(None, alias="address")
    f_landmark: Optional[str] = Field(None, alias="landmark")
    f_city: Optional[str] = Field(None, alias="city")
    f_state: Optional[str] = Field(None, alias="state")
    f_latitude: Optional[float] = Field(None, alias="latitude")
    f_longitude: Optional[float] = Field(None, alias="longitude")

    f_mobile_number: Optional[str] = Field(None, alias="mobile_number")

    f_breakfast_cost: Optional[float] = Field(None, alias="breakfast_cost")
    f_lunch_or_dinner_cost: Optional[float] = Field(None, alias="lunch_or_dinner_cost")
    f_breakfast_and_lunch_or_dinner_cost: Optional[float] = Field(None, alias="breakfast_and_lunch_or_dinner_cost")
    f_lunch_and_dinner_cost: Optional[float] = Field(None, alias="lunch_and_dinner_cost")
    f_thali_cost: Optional[float] = Field(None, alias="thali_cost")
    f_cup_of_rice: Optional[float] = Field(None, alias="cup_of_rice")

    f_dal: Optional[str] = Field(None, alias="dal")
    f_roti: Optional[str] = Field(None, alias="roti")
    f_sabji: Optional[str] = Field(None, alias="sabji")
    f_food_category: Optional[str] = Field(None, alias="food_category")

    f_daily_item: Optional[Any] = Field(None, alias="daily_item")
    f_restructure_menu: Optional[Any] = Field(None, alias="restructure_menu")
    f_subscription: Optional[Any] = Field(None, alias="subscription")
    f_faq: Optional[Any] = Field(None, alias="faq")
    f_mess_rules: Optional[Any] = Field(None, alias="mess_rules")
    f_report: Optional[Any] = Field(None, alias="report")
    f_image_list: Optional[Any] = Field(None, alias="image_list")

    f_disable: Optional[bool] = Field(None, alias="is_disabled")
    f_isDelete: Optional[bool] = Field(None, alias="is_deleted")

    class Config:
        populate_by_name = True



class FoodResponseSchema(BaseModel):
    f_id: int = Field(..., alias="f_id")
    u_id: Optional[int] = Field(None, alias="user_id")

    f_name: str = Field(..., alias="name")
    f_description: Optional[str] = Field(None, alias="description")
    f_type: Optional[str] = Field(None, alias="type")
    f_address: Optional[str] = Field(None, alias="address")
    f_landmark: Optional[str] = Field(None, alias="landmark")
    f_city: Optional[str] = Field(None, alias="city")
    f_state: Optional[str] = Field(None, alias="state")
    f_latitude: Optional[float] = Field(None, alias="latitude")
    f_longitude: Optional[float] = Field(None, alias="longitude")

    f_mobile_number: Optional[str] = Field(None, alias="mobile_number")

    f_breakfast_cost: Optional[float] = Field(None, alias="breakfast_cost")
    f_lunch_or_dinner_cost: Optional[float] = Field(None, alias="lunch_or_dinner_cost")
    f_breakfast_and_lunch_or_dinner_cost: Optional[float] = Field(None, alias="breakfast_and_lunch_or_dinner_cost")
    f_lunch_and_dinner_cost: Optional[float] = Field(None, alias="lunch_and_dinner_cost")
    f_thali_cost: Optional[float] = Field(None, alias="thali_cost")
    f_cup_of_rice: Optional[float] = Field(None, alias="cup_of_rice")

    f_dal: Optional[str] = Field(None, alias="dal")
    f_roti: Optional[str] = Field(None, alias="roti")
    f_sabji: Optional[str] = Field(None, alias="sabji")
    f_food_category: Optional[str] = Field(None, alias="food_category")

    f_daily_item: Optional[Any] = Field(None, alias="daily_item")
    f_restructure_menu: Optional[Any] = Field(None, alias="restructure_menu")
    f_subscription: Optional[Any] = Field(None, alias="subscription")
    f_faq: Optional[Any] = Field(None, alias="faq")
    f_mess_rules: Optional[Any] = Field(None, alias="mess_rules")
    f_report: Optional[Any] = Field(None, alias="report")
    f_image_list: Optional[Any] = Field(None, alias="image_list")

    f_disable: bool = Field(False, alias="is_disabled")
    f_isDelete: bool = Field(False, alias="is_deleted")

    atCreate: datetime = Field(..., alias="created_at")
    atUpdate: datetime = Field(..., alias="updated_at")

    class Config:
        from_attributes = True  # Enables ORM support
        populate_by_name = True
