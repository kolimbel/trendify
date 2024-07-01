import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    def __init__(self, dotenv_path='.env'):
        self.load_env(dotenv_path)

    def load_env(self, dotenv_path):
        load_dotenv(dotenv_path=Path(dotenv_path))
        self.REDIS_HOST = os.getenv('REDIS_HOST')
        self.REDIS_PORT = os.getenv('REDIS_PORT')
        self.REDIS_DB = os.getenv('REDIS_DB')
        self.REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
        self.BACKEND_HOST = os.getenv('BACKEND_HOST')

    @property
    def redis_host(self):
        return self.REDIS_HOST

    @property
    def redis_port(self):
        return self.REDIS_PORT

    @property
    def redis_db(self):
        return self.REDIS_DB

    @property
    def redis_password(self):
        return self.REDIS_PASSWORD

    @property
    def backend_host(self):
        return self.BACKEND_HOST