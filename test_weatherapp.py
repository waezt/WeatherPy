import pytest
import weatherapp

def test_get_coordinates_valid():
    lat, lon = project.get_coordinates("London")
    assert isinstance(lat, float)
    assert isinstance(lon, float)

def test_get_coordinates_invalid():
    with pytest.raises(SystemExit):
        project.get_coordinates("cwjkencjcnwlcnxc") #random text

def test_get_weather_code_valid():
    assert project.get_weather_code("3") == "Overcast"

def test_get_weather_code_invalid():
    assert project.get_weather_code(9999) == "Unknown"


def test_get_hourly_length():
    times, temps = project.get_hourly(51.5, -0.13)  # London coordinates
    assert len(times) == 24
    assert len(temps) == 24


def test_get_weather_has_keys():
    lat, lon = project.get_coordinates("Paris")
    weather = project.get_weather(lat, lon)
    assert "temperature" in weather
    assert "windspeed" in weather
    assert "winddirection" in weather
    assert "weathercode" in weather
