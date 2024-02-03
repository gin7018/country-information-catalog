import json
import os
import zeep

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


