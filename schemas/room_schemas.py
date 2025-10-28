from pydantic import BaseModel,Field
from datetime import datetime,date
from typing import Optional


class RoomCreateSchema(BaseModel):
    r_bills: Optional[str] = Field(None, alias="bills")
    r_city: str = Field(..., alias="city")
    r_commonArea: Optional[str] = Field(None, alias="common_area")
    r_depositAmount: Optional[int] = Field(None, alias="deposit_amount")
    r_disable: bool = Field(False, alias="is_disabled")
    r_double_person_cost: Optional[int] = Field(None, alias="double_person_cost")
    r_family_cost: Optional[int] = Field(None, alias="family_cost")
    r_flat_type: Optional[str] = Field(None, alias="flat_type")
    r_gender_type: Optional[str] = Field(None, alias="gender_type")
    r_home_address: str = Field(..., alias="home_address")
    r_home_faq: Optional[str] = Field(None, alias="home_faq")
    r_home_name: str = Field(..., alias="home_name")
    r_home_rules: Optional[str] = Field(None, alias="home_rules")
    r_image: Optional[str] = Field(None, alias="image")
    r_isDelete: bool = Field(False, alias="is_deleted")
    r_room_available_date: Optional[date] = Field(None, alias="room_available_date")
    r_landmark: str = Field(..., alias="landmark")
    r_latitude: Optional[float] = Field(None, alias="latitude")
    r_longitude: Optional[float] = Field(None, alias="longitude")
    r_meals_available: bool = Field(False, alias="meals_available")
    r_mobile_number: Optional[str] = Field(None, alias="mobile_number")
    r_notice_pride: Optional[int] = Field(None, alias="notice_period")
    r_report: Optional[str] = Field(None, alias="report")
    r_room_category: Optional[str] = Field(None, alias="room_category")
    r_room_facility: Optional[str] = Field(None, alias="room_facility")
    r_room_ownership_type: Optional[str] = Field(None, alias="room_ownership_type")
    r_room_type: Optional[str] = Field(None, alias="room_type")
    r_single_person: Optional[int] = Field(None, alias="single_person_cost")
    r_state: str = Field(..., alias="state")
    r_total_room: Optional[int] = Field(None, alias="total_room")
    r_triple_person_cost: Optional[int] = Field(None, alias="triple_person_cost")
    r_triple_plus_cost: Optional[int] = Field(None, alias="triple_plus_cost")

    class Config:
        populate_by_name = True

class RoomResponseSchema(BaseModel):

    r_id: int =Field(...,alias="room_id")
    atCreate: datetime =Field(...,alias="created_at")
    atUpdate: datetime =Field(...,alias="updated_at")
    r_bills: Optional[str] = Field(None, alias="bills")
    r_city: str = Field(..., alias="city")
    r_commonArea: Optional[str] = Field(None, alias="common_area")
    r_depositAmount: Optional[int] = Field(None, alias="deposit_amount")
    r_disable: bool = Field(False, alias="is_disabled")
    r_double_person_cost: Optional[int] = Field(None, alias="double_person_cost")
    r_family_cost: Optional[int] = Field(None, alias="family_cost")
    r_flat_type: Optional[str] = Field(None, alias="flat_type")
    r_gender_type: Optional[str] = Field(None, alias="gender_type")
    r_home_address: str = Field(..., alias="home_address")
    r_home_faq: Optional[str] = Field(None, alias="home_faq")
    r_home_name: str = Field(..., alias="home_name")
    r_home_rules: Optional[str] = Field(None, alias="home_rules")
    r_image: Optional[str] = Field(None, alias="image")
    r_isDelete: bool = Field(False, alias="is_deleted")
    r_room_available_date: Optional[date] = Field(None, alias="room_available_date")
    r_landmark: str = Field(..., alias="landmark")
    r_latitude: Optional[float] = Field(None, alias="latitude")
    r_longitude: Optional[float] = Field(None, alias="longitude")
    r_meals_available: bool = Field(False, alias="meals_available")
    r_mobile_number: Optional[str] = Field(None, alias="mobile_number")
    r_notice_pride: Optional[int] = Field(None, alias="notice_period")
    r_report: Optional[str] = Field(None, alias="report")
    r_room_category: Optional[str] = Field(None, alias="room_category")
    r_room_facility: Optional[str] = Field(None, alias="room_facility")
    r_room_ownership_type: Optional[str] = Field(None, alias="room_ownership_type")
    r_room_type: Optional[str] = Field(None, alias="room_type")
    r_single_person: Optional[int] = Field(None, alias="single_person_cost")
    r_state: str = Field(..., alias="state")
    r_total_room: Optional[int] = Field(None, alias="total_room")
    r_triple_person_cost: Optional[int] = Field(None, alias="triple_person_cost")
    r_triple_plus_cost: Optional[int] = Field(None, alias="triple_plus_cost")
    u_id: int = Field(..., alias="user_id")

    class Config:
         from_attributes = True
         populate_by_name = True