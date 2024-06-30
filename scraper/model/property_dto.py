from pydantic import BaseModel

from scraper.model.enum.propety_type import PropertyType


class PropertyDto(BaseModel):
    title: str
    description: str
    price: int
    type: PropertyType

    class Config:
        use_enum_values = True
