from typing import Optional

from pydantic import BaseModel, Field


class AddressBase(BaseModel):
    name: str
    phone: Optional[str] = None
    company_name: Optional[str] = None
    address_line1: str
    address_line2: Optional[str] = None
    city_locality: str
    state_province: str
    postal_code: str
    country_code: str = Field(..., min_length=2, max_length=2)
    is_residential: Optional[bool] = False

class AddressCreate(AddressBase):
    pass

class AddressRead(AddressBase):
    id: int

    class Config:
        from_attributes = True