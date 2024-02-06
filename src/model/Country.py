import json


class Country:
    def __init__(self, name, iso_code):
        self.name = name
        self.iso_code = iso_code

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(data):
        return Country(name=data["sName"], iso_code=data["sISOCode"])


class CountryProfile:

    def __init__(self, iso_code, name, capital_city, country_flag, languages):
        self.languages = languages
        self.country_flag = country_flag
        self.capital_city = capital_city
        self.name = name
        self.iso_code = iso_code

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(data):
        languages = data["Languages"]["tLanguage"]
        language_as_tuple = list(map(lambda lang: (lang["sISOCode"], lang["sName"]), languages))

        return CountryProfile(
            iso_code=data["sISOCode"],
            name=data["sName"],
            capital_city=data["sCapitalCity"],
            country_flag=data["sCountryFlag"],
            languages=language_as_tuple
        )
