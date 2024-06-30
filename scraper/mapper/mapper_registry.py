from typing import Dict, Callable, Any
from scraper.model.scraper_data_dto import ScraperDataDto


class MapperRegistry:
    def __init__(self):
        self._registry: Dict[str, Callable[[Dict[str, Any]], ScraperDataDto]] = {}

    def register_mapper(self, source: str, mapper_func: Callable[[Dict[str, Any]], ScraperDataDto]):
        self._registry[source] = mapper_func

    def get_mapper(self, source: str) -> Callable[[Dict[str, Any]], ScraperDataDto]:
        if source not in self._registry:
            raise ValueError(f"No mapper registered for source: {source}")
        return self._registry[source]
