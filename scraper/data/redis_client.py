import redis

from scraper.data.config import Config


class RedisClient:
    def __init__(self, config: Config):
        self._client = redis.Redis(
            host=config.redis_host,
            port=config.redis_port,
            db=config.redis_db,
            password=config.redis_password
        )

    def get(self, key):
        return self._client.get(key)

    def set(self, key, value):
        self._client.set(key, value)

    def delete(self, key):
        self._client.delete(key)
