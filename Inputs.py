from pydantic import BaseModel
class Input (BaseModel) :
    no_guests:int
    room_category:int
    booking_status:int
    revenue_generated:int
