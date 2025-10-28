from sqlalchemy.orm import Session

from model.room_model import RoomModel
from schemas.room_schemas import RoomResponseSchema,RoomCreateSchema


def get_all_room(db: Session):
    return db.query(RoomModel).all()

def create_room(db: Session, roomCreate: RoomCreateSchema ):
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
