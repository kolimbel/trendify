from scraper.model.property_dto import PropertyDto


class LandDto(PropertyDto):
    area: float
    buildable: bool
