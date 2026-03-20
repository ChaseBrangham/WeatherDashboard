import requests
from geoLogic import getWeatherFromLocation
import sqlite3



class WeatherDataManager:
    def __init__(self):
        pass

    def getRecentWeather(self):
        db = sqlite3.connect("weather.db")
        cursor = db.cursor()

        cursor.execute("""
            SELECT city, temp, feels_like, description, humidity
            FROM weather
            ORDER BY id DESC
            LIMIT 5
        """)

        rows = cursor.fetchall()
        db.close()
        return rows

    def getLatestWeather(self):
        db = sqlite3.connect("weather.db")
        cursor = db.cursor()

        cursor.execute("""
            SELECT city, temp, feels_like, description, humidity
            FROM weather
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        db.close()
        return row

    @staticmethod
    def saveIntoDatabase(myLocation):

        data = getWeatherFromLocation(myLocation)
        if type(data) == AttributeError:
            return "Could not find any weather data there..."
        city = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        db = sqlite3.connect("weather.db")
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temp REAL,
                feels_like REAL,
                description TEXT,
                humidity INTEGER
            )
            """)

        cursor.execute("""
            INSERT INTO weather (city, temp, feels_like, description, humidity)
            VALUES (?, ?, ?, ?, ?)
            """, (city, temp, feels_like, description, humidity))

        db.commit()
        db.close()

        print(f"City: {city}")
        print(f"Temperature: {temp}°F")
        print(f"Feels like: {feels_like}°F")
        print(f"Conditions: {description}")
        print(f"Humidity: {humidity}%")
        print("CITY", city)
        return city

