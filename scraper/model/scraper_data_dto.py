from pydantic import BaseModel
from typing import Union, Any
from scraper.model.house_dto import HouseDto
from scraper.model.apartment_dto import ApartmentDto
from scraper.model.land_dto import LandDto


class ScraperDataDto(BaseModel):
    property_data: Union[HouseDto, ApartmentDto, LandDto]
