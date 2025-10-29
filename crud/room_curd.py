from sqlalchemy.orm import Session
from websockets.legacy.server import HTTPResponse

from model.room_model import RoomModel
from schemas.room_schemas import RoomResponseSchema, RoomCreateSchema, RoomUpdateSchema


def get_all_room_operation(db: Session):
    return db.query(RoomModel).all()

def create_room_operation(db: Session, roomCreate: RoomCreateSchema):
    room = RoomModel(
    r_bills=roomCreate.r_bills,
    r_city =roomCreate.r_city,
    r_commonArea = roomCreate.r_commonArea,
    r_depositAmount =   roomCreate.r_depositAmount,
    r_disable =  roomCreate.r_disable,
    r_double_person_cost = roomCreate.r_double_person_cost,
    r_family_cost =  roomCreate.r_family_cost,
    r_flat_type = roomCreate.r_flat_type,
    r_gender_type = roomCreate.r_gender_type,
    r_home_address = roomCreate.r_home_address,
    r_home_faq =  roomCreate.r_home_faq,
    r_home_name = roomCreate.r_home_name,
    r_home_rules = roomCreate.r_home_rules,
    r_image =  roomCreate.r_image,
    r_isDelete =  roomCreate.r_isDelete,
    r_room_available_date =  roomCreate.r_room_available_date,
    r_landmark =  roomCreate.r_landmark,
    r_latitude =  roomCreate.r_latitude,
    r_longitude = roomCreate.r_longitude,
    r_meals_available =  roomCreate.r_meals_available,
    r_mobile_number =  roomCreate.r_mobile_number,
    r_notice_pride =  roomCreate.r_notice_pride,
    r_report = roomCreate.r_report,
    r_room_category = roomCreate.r_room_category,
    r_room_facility =  roomCreate.r_room_facility,
    r_room_ownership_type =  roomCreate.r_room_ownership_type,
    r_room_type = roomCreate.r_room_type,
    r_single_person =  roomCreate.r_single_person,
    r_state =  roomCreate.r_state,
    r_total_room =  roomCreate.r_total_room,
    r_triple_person_cost = roomCreate.r_triple_person_cost,
    r_triple_plus_cost =  roomCreate.r_triple_plus_cost,
    u_id = 1,
    )

    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def update_room_operation(db: Session, r_id:int, roomUpdate: RoomUpdateSchema):
    db_room = db.query(RoomModel).filter(RoomModel.r_id == r_id).first()
    if not db_room:
         raise HTTPResponse(status_code=404, detail="Room not found")

    update_data = roomUpdate.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_room, key, value)

    db.commit()
    db.refresh(db_room)
    return db_room

def delete_room_operation(db: Session, r_id:int):
    db_room = db.query(RoomModel).filter(RoomModel.r_id == r_id).first()

    if not db_room:
        raise HTTPResponse(status_code=404, detail="Room not found")

    db.delete(db_room)
    db.commit()
    return True

def search_room_operation(db: Session,  home_name: str = None,
    city: str = None,
    state: str = None,
    address: str = None,
    flat_type: str = None,
    gender_type: str = None,
    min_price: int = None,
    max_price: int = None):
    query = db.query(RoomModel).filter(RoomModel.r_isDelete == False)

    if home_name:
        query = query.filter(RoomModel.r_home_name.ilike(f"%{home_name}%"))
    if city:
        query = query.filter(RoomModel.r_city.ilike(f"%{city}%"))
    if state:
        query = query.filter(RoomModel.r_state.ilike(f"%{state}%"))
    if address:
        query = query.filter(RoomModel.r_home_address.ilike(f"%{address}%"))
    if flat_type:
        query = query.filter(RoomModel.r_flat_type.ilike(f"%{flat_type}%"))
    if gender_type:
        query = query.filter(RoomModel.r_gender_type.ilike(f"%{gender_type}%"))
    if min_price:
        query = query.filter(RoomModel.r_single_person >= min_price)
    if max_price:
        query = query.filter(RoomModel.r_single_person <= max_price)

    return query.all()


