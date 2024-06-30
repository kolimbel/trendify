from scraper.mapper.mapper_registry import MapperRegistry
from scraper.mapper.service1_mapper import map_service1_to_dto
from scraper.service.scraper_service import ScraperService


class Main:

    def __init__(self):
        self._mapper_registry = MapperRegistry()

    @staticmethod
    def mock_fetch_raw_data(source: str) -> dict:
        if source == "service1":
            return {
                "property_type": "house",
                "title": "Beautiful House",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "price": 300000,
                "num_rooms": 5,
                "garden_size": 50.5
            }
        else:
            raise ValueError(f"Unknown source: {source}")

    def register_all_mappers(self):
        self._mapper_registry.register_mapper("service1", map_service1_to_dto)

    def run(self):
        self.register_all_mappers()

        sources = ["service1"]

        for source in sources:
            raw_data = self.mock_fetch_raw_data(source)
            mapper = self._mapper_registry.get_mapper(source)
            dto = mapper(raw_data)
            ScraperService.send_to_api(dto)


if __name__ == '__main__':
    main = Main()
    main.run()
