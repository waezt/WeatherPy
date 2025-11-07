import csv
import sys
from tabulate import tabulate
import requests
from datetime import datetime
import matplotlib.pyplot as plt


now = datetime.now()
time_str = now.strftime("%H:%M:%S")     #current time

def get_coordinates(city):
    '''
    Converts city name into its geographical coordinates.

    :param city: Name of city
    :type city: str
    :raise IndexError: If city not found
    :return: latitude and longitude
    :rtype: float
    '''
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json"}
    response = requests.get(url, params=params, headers={"User-Agent": "weather-app"})
    data = response.json()
    try:
        return float(data[0]["lat"]), float(data[0]["lon"])
    except IndexError:
        sys.exit("City not found")

def get_weather(lat, lon):
    '''
    Uses coordinates to retrieve location weather

    :param lat, lon: Coordinates of city
    :type late, lon: float
    :return: Current weather data including temperature, wind, and code.
    :rtype: dict
    '''
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params)
    return response.json()["current_weather"]

def get_weather_code(c):
    with open("weather_codes.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if str(row["code"]) == c:
                return row["description"]
    return "Unknown"

def get_hourly(lat, lon):
    '''
    Uses coordinates to retrieve hourly loaction weather

    :param lat, lon: Coordinates of city
    :type late, lon: float
    :return: Hourly weather data including temperature and time for past 24 hours.
    :rtype: str
    '''
    url = "https://api.open-meteo.com/v1/forecast"
    params_2 = {"latitude": lat, "longitude": lon, "hourly": "temperature_2m"}
    response = requests.get(url, params=params_2)
    times = response.json()["hourly"]["time"]
    times = times[-24:] #only gets 24 hours
    times = [t[-5:] for t in times] #clean up string to only show time
    temperature = response.json()["hourly"]["temperature_2m"]
    temperature = temperature[-24:] #past 24 hours only
    return times, temperature

def plot_graph(x, y):
    plt.style.use("seaborn-v0_8-darkgrid")
    plt.plot(x, y, marker="o", linestyle="-", color="dodgerblue", linewidth=2, markersize=6)
    plt.title("24 Hour View")
    plt.xlabel("Time")
    plt.ylabel("Temperature / °C")
    plt.show()



def main():
    while True:
        try:
            city = input("Enter a City: ").strip().capitalize()
            if city == "":
                raise ValueError
            else:
                break
        except ValueError:
            print("Empty city name")

    latitude, longitude = get_coordinates(city)
    weather = get_weather(latitude, longitude)
    description = get_weather_code(str(weather["weathercode"]))

    table = [
        ["Temperature (°C)", weather["temperature"]],
        ["Wind Speed (km/h)", weather["windspeed"]],
        ["Wind Direction (°)", weather["winddirection"]],
        ["Description", description],
        ["Time", time_str]
    ]
    print(tabulate(table, headers=["Metric", "Value"], tablefmt="fancy_grid"))

    time, temp = get_hourly(latitude, longitude)
    view_graph = input("24 hour view? (yes/no) ").strip().capitalize()
    if view_graph == "Yes":
        plot_graph(time, temp)
    else:
        sys.exit()





if __name__ == "__main__":
    main()

