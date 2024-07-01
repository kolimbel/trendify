from scraper.data.containers import Container
from scraper.mapper.mapper_registry import MapperRegistry
from scraper.mapper.service1_mapper import map_service1_to_dto
from scraper.service.cache_service import CacheService
from scraper.service.scraper_service import ScraperService


class Main:

    def __init__(self):
        self._scraper_service: ScraperService = None
        self._cache_service: CacheService = None
        self._mapper_registry: MapperRegistry = MapperRegistry()

    @staticmethod
    def mock_fetch_raw_data(source: str) -> dict:
        if source == "service1":
            return {
                "external_id": 123,
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

    def init_container(self):
        container = Container()
        self._cache_service = container.cache_service()
        self._scraper_service = container.scraper_service()

    def run(self):
        self.register_all_mappers()

        sources = ["service1"]

        for source in sources:
            raw_data = self.mock_fetch_raw_data(source)
            mapper = self._mapper_registry.get_mapper(source)
            dto = mapper(raw_data)
            self._cache_service.set_value(dto.property_data.external_id, dto.property_data.model_dump_json().__str__())
            self._scraper_service.send_to_api(dto)


if __name__ == '__main__':
    main = Main()
    main.init_container()
    main.run()
