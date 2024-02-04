import requests


api_endpoint = ("https://cdn.jsdelivr.net/gh/fawazahmed0/"
                "currency-api@1/latest/")


def convert_currency(from_currency_iso_code, to_currency_iso_code) -> float:
    currency_endpoint = api_endpoint + f"currencies/{from_currency_iso_code}/{to_currency_iso_code}.json"

    result = requests.get(
        url=currency_endpoint
    ).json()
    print(result)
    return float(result[to_currency_iso_code])
