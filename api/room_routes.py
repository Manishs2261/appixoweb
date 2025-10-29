from typing import List,Optional
from sqlalchemy.orm import Session
from schemas import room_schemas
from  core.database import get_db
from crud import room_curd
from fastapi import APIRouter,Depends,HTTPException,status,Query

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/", response_model=List[room_schemas.RoomResponseSchema])
def get_all_rooms(db:Session = Depends(get_db)):
    return room_curd.get_all_room_operation(db)


@router.post("/" , response_model=room_schemas.RoomResponseSchema)
def create_room(new_room:room_schemas.RoomCreateSchema,db: Session = Depends(get_db)):
    return room_curd.create_room_operation(db, new_room)

@router.patch("/{roomId}", response_model=room_schemas.RoomResponseSchema)
def update_room_endpoint(
    roomId: int,
    room_update: room_schemas.RoomUpdateSchema,
    db: Session = Depends(get_db)
):
    updated_room = room_curd.update_room_operation(db, roomId, room_update)

    if not updated_room:
        raise HTTPException(status_code=404, detail="Room not found")

    return updated_room

@router.delete("/{roomId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_room(roomId:int, db: Session = Depends(get_db)):
    result = room_curd.delete_room_operation(db,roomId)
    if not result:
        raise HTTPException(status_code=404, detail="Room not found")

    return {"message": "Room deleted"}

@router.get("/search", response_model=List[room_schemas.RoomResponseSchema])
def search_rooms(db: Session = Depends(get_db),
                 home_name: Optional[str] = Query(None),
                 city: Optional[str] = Query(None),
                 state: Optional[str] = Query(None),
                 address: Optional[str] = Query(None),
                 flat_type: Optional[str] = Query(None),
                 gender_type: Optional[str] = Query(None),
                 min_price: Optional[int] = Query(None),
                 max_price: Optional[int] = Query(None),
                 ):
    results = room_curd.search_room_operation(
        db=db,
        home_name=home_name,
        city=city,
        state=state,
        address=address,
        flat_type=flat_type,
        gender_type=gender_type,
        min_price=min_price,
        max_price=max_price,
    )

    return results