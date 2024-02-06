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


def get_capital_city_by_cc(country_code: str) -> str:
    result = client.service.CapitalCity(country_code.upper())
    return result


def get_country_profile(country_code: str) -> CountryProfile:
    result = client.service.FullCountryInfo(country_code.upper())
    country_profile = CountryProfile.from_json(result)
    return country_profile


def get_currency_code_by_cc(country_code: str) -> str:
    result = client.service.CountryCurrency(country_code.upper())
    print(f"{country_code}'s currency: {result}")
    return result["sISOCode"]


if __name__ == '__main__':
    # get_all_country_names_local()
    # get_capital_city_by_country_name("Belgium")
    # info = get_country_profile("Belgium")
    # print(info)
    # cc = get_currency_code_by_cc(info.iso_code)
    # convert_currency(cc.lower(), "usd")
    print(get_capital_city_by_cc("BE"))
