from core.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'users'

    u_id = Column(Integer, primary_key=True, index=True)
    u_name = Column(String(100))
    u_email = Column(String(100), unique=True, index=True ,nullable=False)
    u_mobile_number = Column(String(20))
    u_age = Column(Integer)
    u_gender = Column(String(10))
    atCreate = Column(DateTime, default=datetime.utcnow)
    atUpdate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    rooms = relationship("RoomModel",back_populates="user",cascade="all, delete-orphan")