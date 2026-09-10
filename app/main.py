import os
import requests


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")

    city = "Paris"
    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params,
    )

    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )

if __name__ == "__main__":
    get_weather()
