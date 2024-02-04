import json
import os
import zeep

from src.handler.CurrencyConverterDataHandler import convert_currency
from src.model.Country import Country, CountryProfile

country_info_wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=country_info_wsdl_url)


def get_all_country_names(use_api=False) -> list[Country]:
    country_dict_lst: list
    if use_api:
        country_dict_lst = client.service.ListOfCountryNamesByName()
    else:
        file_path = os.path.join(os.path.dirname(__file__), '../resources/countries.json')
        country_dict_lst = json.load(open(file_path))
    countries = list(map(lambda ct: Country.from_json(ct), country_dict_lst))
    return countries


def get_capital_city_by_country_name(country_name: str) -> str:
    all_countries = get_all_country_names()
    country_info: Country = list(filter(lambda country:
                                        country.name == country_name, all_countries))[0]
    result = client.service.CapitalCity(country_info.iso_code)
    return result


def get_country_profile(country_name: str) -> CountryProfile:
    all_countries = get_all_country_names()
    basic_country_info: Country = list(filter(lambda country:
                                              country.name == country_name, all_countries))[0]
    result = client.service.FullCountryInfo(basic_country_info.iso_code)
    country_profile = CountryProfile.from_json(result)
    return country_profile


def get_currency_code_by_country_code(country_code: str) -> str:
    result = client.service.CountryCurrency(country_code)
    print(f"{country_code}'s currency: {result}")
    return result["sISOCode"]


if __name__ == '__main__':
    # get_all_country_names_local()
    # get_capital_city_by_country_name("Belgium")
    info = get_country_profile("Belgium")
    print(info)
    cc = get_currency_code_by_country_code(info.iso_code)
    convert_currency(cc.lower(), "usd")
