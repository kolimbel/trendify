from typing import Optional

from scraper.model.property_dto import PropertyDto


class ApartmentDto(PropertyDto):
    floor: int
    balcony: Optional[bool] = None
