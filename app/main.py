import os
import requests
from dotenv import (
    load_dotenv,
)

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    print(
        f"Weather in {CITY}: "
        f"{data["current"]["condition"]["text"]}, "
        f"{data["current"]["temp_c"]}°C"
    )


if __name__ == "__main__":
    get_weather()
