import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_API_URL")

def fetch_data(endpoint, params=None):
    """
    Fetch data from the OpenF1 API and return it as a DataFrame.

    Args:
        endpoint (str): API endpoint (e.g., "meetings", "sessions").
        params (dict): Optional query parameters for the API.

    Returns:
        pd.DataFrame: DataFrame containing the API response data.

    Notes:
        The OpenF1 API requires properly URL-encoded query strings,
        especially when using complex filters (e.g., strings with spaces).
        Using `requests.get(url, params=params)` sometimes causes issues with
        formatting, so we manually prepare the full URL using `requests.Request`.
    """
    if params is None:
        params = {}

    url = f"{BASE_URL}{endpoint}"
    full_url = requests.Request('GET', url, params=params).prepare().url
    response = requests.get(full_url)
    response.raise_for_status()
    return pd.DataFrame(response.json())

def fetch_car_data(session_key, driver_number):
    """
    Some data about each car, at a sample rate of about 3.7 Hz.
    """
    return fetch_data("car_data", {"session_key": session_key, "driver_number": driver_number})

# car_data = fetch_car_data(9161, 4)
# print(car_data)

def fetch_drivers(session_key):
    """
    Provides information about drivers for each session.
    """
    return fetch_data("drivers", {"session_key": session_key})

# drivers = fetch_drivers("latest")
# print(drivers)

def fetch_intervals(session_key):
    """
    Fetches real-time interval data between drivers and their gap to the race leader. Available during races only, with updates approximately ever 4 seconds.
    """
    return fetch_data("intervals", {"session_key": session_key})

# intervals = fetch_intervals("latest")
# print(intervals)

def fetch_laps(session_key):
    """
    Provides detailed information about individual laps.
    """
    return fetch_data("laps", {"session_key": session_key})

# laps = fetch_laps(9161)
# print(laps)

def fetch_locations(session_key, driver_number):
    """
    The approximate location of the cars on the circuit, at a sample rate of about 3.7 Hz. USeful for gauging their progess along the track, but lacks details about lateral placement - i.e. whether the car is on the left ot right side of the track. The origin point (0, 0, 0) appears to be arbitrary and not tied to any specific location on the track. 
    """
    return fetch_data("location", {"session_key": session_key, "driver_number": driver_number})

# location = fetch_locations(9161, 4)
# print(location)

def fetch_meetings(year, country):
    """
    Provides information about meetings. A meeting refers to a Grand Prix or testing weekedn and usually includes multiple sessions (practice, qualifying, race, ...).
    """
    return fetch_data("meetings", {"year": year, "country_name": country})

# meetings = fetch_meetings(2023, "Singapore")
# print(meetings)

def fetch_overtakes_beta(session_key, overtaking_driver):
    """
    Provides information about overtakes. AN overtake refers to one driver (the overtaking driver) exchanging positions with another driver (the overtaken driver). This includes both on-track passes and position changes resulting from pit stops or post-race penalties. This data is only available during races and may be incomplete.
    """
    return fetch_data("overtakes", {"session_key": session_key, "overtaking_driver": overtaking_driver})

def fetch_pit(session_key):
    """
    Provides information about cars going through the pit lane.
    """
    return fetch_data("pit", {"session_key": session_key})

# pit = fetch_pit(9161)
# print(pit)

def fetch_position(session_key):
    """
    Provides driver positions throughout a session, including initial placement and subsequent changes
    """
    return fetch_data("position", {"session_key": session_key})

# positions = fetch_position(9161)
# print(positions)

def fetch_race_control(session_key):
    """
    Proivdes information about race control (racing incidents, flags, safety car, ...)
    """
    return fetch_data("race_control", {"session_key": session_key})

# race_control = fetch_race_control(9161)
# print(race_control)

def fetch_sessions(session_key):
    """
    Provides information about sessions. A session refers to a distinct period of track activity during a Grand Prix or testing weekend (practice, qualifying, sprint, race, ...)
    """
    return fetch_data("sessions", {"session_key": session_key})

# sessions = fetch_sessions("latest")
# print(sessions)

def fetch_session_results(session_key):
    """
    Provides standings after a session.
    """
    return fetch_data("session_result", {"session_key": session_key})

# session_result = fetch_session_results(9161)
# print(session_result)

def fetch_starting_grid(session_key):
    """
    Provides the starting grid for the upcoming race.
    """
    return fetch_data("starting_grid", {"session_key": session_key})

# grid = fetch_starting_grid(9161)
# print(grid)

def fetch_stints(session_key):
    """
    Provides information about individual stints. A stint refers to a period of continuous driving by a driver during a session.
    """
    return fetch_data("stints", {"session_key": session_key})

# stint = fetch_stints(9161)
# print(stint)

def fetch_team_radio(session_key):
    """
    Provides a collection of radio exchanges between drivers and their teams during sessions. Note that only a limited selection of communication are included, not the complete record of radio interactions.
    """
    return fetch_data("team_radio", {"session_key": session_key})

# radio = fetch_team_radio(9161)
# print(radio)

def fetch_weather(session_key):
    """
    Provides the weather over the track, updated every minute.
    """
    return fetch_data("weather", {"session_key": session_key})

# weather = fetch_weather(9161)
# print(weather)