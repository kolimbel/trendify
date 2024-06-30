from typing import Dict, Any

from scraper.model.apartment_dto import ApartmentDto
from scraper.model.enum.propety_type import PropertyType
from scraper.model.house_dto import HouseDto
from scraper.model.land_dto import LandDto
from scraper.model.scraper_data_dto import ScraperDataDto


def map_service1_to_dto(raw_data: Dict[str, Any]) -> ScraperDataDto:
    property_type = raw_data.get("property_type")
    if property_type == "house":
        property_data = HouseDto(
            title=raw_data.get("title"),
            description=raw_data.get("description"),
            price=raw_data.get("price"),
            num_rooms=raw_data.get("num_rooms"),
            garden_size=raw_data.get("garden_size"),
            type=PropertyType.HOUSE
        )
    elif property_type == "apartment":
        property_data = ApartmentDto(
            title=raw_data.get("title"),
            description=raw_data.get("description"),
            price=raw_data.get("price"),
            floor=raw_data.get("floor"),
            balcony=raw_data.get("balcony"),
            type=PropertyType.APARTMENT
        )
    elif property_type == "land":
        property_data = LandDto(
            title=raw_data.get("title"),
            description=raw_data.get("description"),
            price=raw_data.get("price"),
            area=raw_data.get("area"),
            buildable=raw_data.get("buildable"),
            type=PropertyType.LAND
        )
    else:
        raise ValueError(f"Unknown property type: {property_type}")

    return ScraperDataDto(property_data=property_data)
