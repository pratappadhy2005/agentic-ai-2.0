from pydantic import BaseModel, field_validator, model_validator, computed_field, Field
from typing import Optional


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: Optional[int] = Field(ge=1, le=30)
    rate_per_night: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.rate_per_night

    @model_validator(mode="after")
    def check_total_price(self):
        if self.total_price > 1000:
            raise ValueError("Total price cannot exceed 1000")
        return self


booking = Booking(
    user_id=1,
    room_id=1,
    nights=5,
    rate_per_night=50,
)

print(booking.total_price)
