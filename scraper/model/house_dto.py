from scraper.model.property_dto import PropertyDto


class HouseDto(PropertyDto):
    num_rooms: int
    garden_size: float
