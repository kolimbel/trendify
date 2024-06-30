import requests
from scraper.model.scraper_data_dto import ScraperDataDto


class ScraperService:

    @staticmethod
    def send_to_api(dto: ScraperDataDto):
        url = "http://localhost:8080/api/v1/scraper/data-test"
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
