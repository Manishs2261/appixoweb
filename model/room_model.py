from sqlalchemy import Column,Integer,String,DateTime,Text,Boolean,Date,Double,ForeignKey
from datetime import datetime
from core.database import Base
from sqlalchemy.orm import  relationship


class RoomModel(Base):
    __tablename__ = "rooms"

    r_id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    atCreate = Column(DateTime,default=datetime.utcnow)
    atUpdate = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    r_bills = Column(Text)
    r_city =Column(String(255),nullable=False)
    r_commonArea = Column(Text)
    r_depositAmount = Column(Integer)
    r_disable = Column(Boolean, default=False)
    r_double_person_cost = Column(Integer)
    r_family_cost = Column(Integer)
    r_flat_type = Column(String(255))
    r_gender_type = Column(String(255))
    r_home_address = Column(String(255),nullable=False)
    r_home_faq = Column(Text)
    r_home_name = Column(String(255),nullable=False)
    r_home_rules = Column(Text)
    r_image = Column(Text)
    r_isDelete = Column(Boolean,default=False)
    r_room_available_date = Column(Date)
    r_landmark = Column(String(255), nullable=False)
    r_latitude = Column(Double)
    r_longitude = Column(Double)
    r_meals_available = Column(Boolean,default=False)
    r_mobile_number = Column(String(255))
    r_notice_pride = Column(Integer)
    r_report = Column(Text)
    r_room_category = Column(Text)
    r_room_facility = Column(Text)
    r_room_ownership_type = Column(String(255))
    r_room_type = Column(String(255))
    r_single_person = Column(Integer)
    r_state = Column(String(255),nullable=False)
    r_total_room = Column(Integer)
    r_triple_person_cost = Column(Integer)
    r_triple_plus_cost = Column(Integer)
    u_id = Column(Integer,ForeignKey("users.u_id",ondelete="CASCADE"),nullable=False)

    user = relationship("UserModel",back_populates="rooms")





