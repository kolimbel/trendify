class CacheService:
    def __init__(self, cache_client):
        self._cache_client = cache_client

    def get_value(self, key):
        return self._cache_client.get(key)

    def set_value(self, key, value):
        self._cache_client.set(key, value)

    def delete_value(self, key):
        self._cache_client.delete(key)
