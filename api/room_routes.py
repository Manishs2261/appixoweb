from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session
from schemas import room_schemas
from  core.database import get_db
from crud import room
from fastapi import APIRouter

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/", response_model=List[room_schemas.RoomResponseSchema])
def get_all_rooms(db:Session = Depends(get_db)):
    return room.get_all_room(db)


@router.post("/" , response_model=room_schemas.RoomResponseSchema)
def create_room(new_room:room_schemas.RoomCreateSchema,db: Session = Depends(get_db)):
    return room.create_room(db, new_room)