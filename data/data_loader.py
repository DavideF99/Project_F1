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

def fetch_drivers(session_key):
    return fetch_data("drivers", {"session_key": session_key})

# drivers = fetch_drivers("latest"-1)
# print(drivers)
