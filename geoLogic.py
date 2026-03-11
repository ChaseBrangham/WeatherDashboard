from geopy.geocoders import Nominatim
import requests



def getWeatherFromLocation(myLocation: str):
    if myLocation is None:
        print("Could not find that location.")
        raise SystemExit

    geolocator = Nominatim(user_agent="WeatherDashboard")
    print("Requesting location:", myLocation)
    location = geolocator.geocode(str(myLocation)) #  i.e. San Diego, California
    API_KEY = "2f787e4e5b30b11cf92f8350f09e21b9"
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

