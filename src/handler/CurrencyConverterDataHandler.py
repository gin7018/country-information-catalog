from typing import Optional

import requests


api_endpoint = ("https://cdn.jsdelivr.net/gh/fawazahmed0/"
                "currency-api@1/latest/")


def convert_currency(from_currency_iso_code, to_currency_iso_code, amount: float) -> Optional[float]:
    print(f"converting from {from_currency_iso_code} to {to_currency_iso_code}")
    currency_endpoint = api_endpoint + f"currencies/{from_currency_iso_code.lower()}/{to_currency_iso_code.lower()}.json"

    result = requests.get(
        url=currency_endpoint
    )
    print(result)
    if result.status_code == 200:
        multiplier = result.json()[to_currency_iso_code.lower()]
        return multiplier
    return None


if __name__ == '__main__':
    print(convert_currency("usd", "usd", 34))