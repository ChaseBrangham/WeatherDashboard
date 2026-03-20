from dotenv import load_dotenv
import os
from geopy.geocoders import Nominatim
import requests


def getWeatherFromLocation(myLocation: str):
    if myLocation is None:
        print("Could not find that location.")
        raise SystemExit

    geolocator = Nominatim(user_agent="WeatherDashboard")
    print("Requesting location:", myLocation)
    location = geolocator.geocode(str(myLocation)) #  i.e. San Diego, California

    load_dotenv()
    API_KEY = os.getenv("API_KEY")


    try:
        lat = location.latitude
        lon = location.longitude
        print(lat, lon)
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "imperial"
        }
        response = requests.get(url, params=params)

        print("Request URL:", response.url)
        print("Status:", response.status_code)

        data = response.json()
        return data
    except AttributeError as e:
        return e

