from dependency_injector import containers, providers

from scraper.data.config import Config
from scraper.data.redis_client import RedisClient
from scraper.service.cache_service import CacheService
from scraper.service.scraper_service import ScraperService


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Config, dotenv_path='.env')
    redis_client = providers.Factory(RedisClient, config=config)
    cache_service = providers.Factory(CacheService, cache_client=redis_client)
    scraper_service = providers.Factory(ScraperService, config=config)