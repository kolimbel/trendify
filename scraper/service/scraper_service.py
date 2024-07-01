import requests

from scraper.data.config import Config
from scraper.model.scraper_data_dto import ScraperDataDto


class ScraperService:
    def __init__(self, config: Config):
        self._host = config.BACKEND_HOST

    def send_to_api(self, dto: ScraperDataDto):
        url = f"{self._host}/api/v1/scraper/data-test"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=dto.model_dump())

        print(response.request.body)
        pass

        if response.status_code == 200:
            print("Data successfully sent to API")
        else:
            print(f"Failed to send data to API, status code: {response.status_code}")
