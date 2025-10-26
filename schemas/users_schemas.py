from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    u_id: int
    u_name: str
    u_email: str
    u_mobile_number: str
    u_age: int
    u_gender: str
    atCreate: datetime
    atUpdate: datetime

    class Config:
        orm_mode = True