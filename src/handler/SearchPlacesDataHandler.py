import os

import requests

from src.model.Place import Place

api_endpoint = "https://api.tomtom.com/search/2/categorySearch/.json"
API_KEY = "G7MaOtAd1WAFEDLz7c1EAqahFyU3SzHD"


def get_restaurants_in_country(country_code: str) -> list[Place]:
    if not API_KEY:
        return []
    # print("api key is set in resto")
    result = requests.get(
        url=api_endpoint,
        headers={
            "content-type": "application/json"
        },
        params={
            "key": API_KEY,
            "countrySet": country_code.upper(),
            "categorySet": "7315",
            "relatedPois": "child"
        }
    ).json()

    places = list(map(lambda obj: Place.from_json(obj), result["results"]))
    return places


def get_tourist_attractions_in_country(country_code: str) -> list[Place]:
    if not API_KEY:
        return []
    # print("api key is set in tourist")
    result = requests.get(
        url=api_endpoint,
        headers={
            "content-type": "application/json"
        },
        params={
            "key": API_KEY,
            "countrySet": country_code.upper(),
            "categorySet": "7376",
            "relatedPois": "all"
        }
    ).json()

    # print(result)
    places = list(map(lambda obj: Place.from_json(obj), result["results"]))
    return places





