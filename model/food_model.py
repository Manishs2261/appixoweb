from core.database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, JSON, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime


class FoodModel(Base):
    __tablename__ = "food_shop"

    f_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Key → users.u_id
    u_id = Column(Integer, ForeignKey("users.u_id", onupdate="CASCADE", ondelete="SET NULL"))

    # Basic Info
    f_name = Column(String(255), nullable=False)
    f_description = Column(String)
    f_type = Column(String(100))  # e.g. Mess, Restaurant, Dhaba, etc.

    # Address
    f_address = Column(String(255))
    f_landmark = Column(String(255))
    f_city = Column(String(100))
    f_state = Column(String(100))
    f_latitude = Column(DECIMAL(10, 7))
    f_longitude = Column(DECIMAL(10, 7))

    # Contact
    f_mobile_number = Column(String(20))

    # Pricing
    f_breakfast_cost = Column(DECIMAL(10, 2))
    f_lunch_or_dinner_cost = Column(DECIMAL(10, 2))
    f_breakfast_and_lunch_or_dinner_cost = Column(DECIMAL(10, 2))
    f_lunch_and_dinner_cost = Column(DECIMAL(10, 2))
    f_thali_cost = Column(DECIMAL(10, 2))
    f_cup_of_rice = Column(DECIMAL(10, 2))

    # Menu Items
    f_dal = Column(String(100))
    f_roti = Column(String(100))
    f_sabji = Column(String(100))
    f_food_category = Column(String(50))

    # JSON Data
    f_daily_item = Column(JSON)
    f_restructure_menu = Column(JSON)
    f_subscription = Column(JSON)
    f_faq = Column(JSON)
    f_mess_rules = Column(JSON)
    f_report = Column(JSON)
    f_image_list = Column(JSON)

    # Flags
    f_disable = Column(Boolean, default=False)
    f_isDelete = Column(Boolean, default=False)

    # Timestamps
    atCreate = Column(DateTime, default=datetime.utcnow)
    atUpdate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to User
    user = relationship("UserModel", back_populates="foods")
