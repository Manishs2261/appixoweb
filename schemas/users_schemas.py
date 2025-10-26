from typing import Optional

from pydantic import BaseModel,Field
from datetime import datetime


class UserUpdateSchema(BaseModel):
    u_name: Optional[str] = Field(None, alias="name")
    u_email: Optional[str] = Field(None, alias="email")
    u_mobile_number: Optional[str] = Field(None, alias="mobile")
    u_age: Optional[int] = Field(None, alias="age")
    u_gender: Optional[str] = Field(None, alias="gender")

    class Config:
        populate_by_name = True

class UserCreateSchema(BaseModel):
    u_name: str = Field(..., alias="name")
    u_email: str = Field(..., alias="email")
    u_mobile_number: str | None = Field(None, alias="mobile_number")
    u_age: int | None = Field(None, alias="age")
    u_gender: str | None = Field(None, alias="gender")

    class Config:
        populate_by_name = True

class UserResponseSchema(BaseModel):
    u_id: int = Field(..., alias="id")
    u_name: str = Field(..., alias="name")
    u_email: str = Field(..., alias="email")
    u_mobile_number: str = Field(..., alias="mobile_number")
    u_age: int = Field(..., alias="age")
    u_gender: str = Field(..., alias="gender")
    atCreate: datetime = Field(..., alias="created_at")
    atUpdate: datetime = Field(..., alias="updated_at")

    class Config:
        from_attributes = True
        populate_by_name = True