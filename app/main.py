import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    CITY = "Kiev"
    URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

    response = requests.get(URL)
    data = response.json()

    print(f"Weather in {CITY}: {data['current']['condition']['text']}, {data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
