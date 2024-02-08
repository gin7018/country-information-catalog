import http

from flask import Flask, request, Blueprint

import src.handler.CountryDataHandler as country_handler
import src.handler.CurrencyConverterDataHandler as currency_handler
import src.handler.SearchPlacesDataHandler as places

app = Flask(__name__)

country_controller = Blueprint("country", __name__, url_prefix="/country")
currency_conv_controller = Blueprint("currency", __name__, url_prefix="/currency")
places_controller = Blueprint("places", __name__, url_prefix="/places")


@country_controller.after_request
@currency_conv_controller.after_request
@places_controller.after_request
def add_access_control_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@country_controller.get("/all")
def get_all_country_names():
    try:
        result = country_handler.get_all_country_names()
        jj = list(map(lambda country: country.toJson(), result))
        return jj
    except Exception as e:
        print(f"something wrong happened {e}")
    return []


@country_controller.get("/profile/<country_code>")
def get_country_profile(country_code: str):
    try:
        result = country_handler.get_country_profile(country_code)
        if not result:
            return '', http.HTTPStatus.NOT_FOUND.value
        return result.toJson()
    except Exception as e:
        print(e)
    return '', http.HTTPStatus.NOT_FOUND.value


@country_controller.get("/currency/<country_code>")
def get_currency_code_by_country_code(country_code: str):
    try:
        result = country_handler.get_currency_code_by_cc(country_code)
        if not result:
            return '', http.HTTPStatus.NOT_FOUND.value
        return result
    except Exception as e:
        print(e)
    return '', http.HTTPStatus.NOT_FOUND.value


@currency_conv_controller.get("/convert")
def convert_currency():
    try:
        from_currency: str = request.args.get("from_currency", "us")
        to_currency: str = request.args.get("to_currency", "eur")
        amount: float = request.args.get("amount", 1)
        result = currency_handler.convert_currency(from_currency, to_currency, amount)
        return str(result)
    except Exception as e:
        print(f"error happened {e}")
    return '', http.HTTPStatus.NOT_FOUND.value


@places_controller.get("/restaurants/<country_code>")
def get_restaurants_in_country(country_code: str):
    try:
        results = places.get_restaurants_in_country(country_code)
        restaurants = list(map(lambda place: place.toJson(), results))
        return restaurants
    except Exception as e:
        print(f"error happened {e}")
    return []


@places_controller.get("/tourist/<country_code>")
def get_tourist_attractions_in_country(country_code: str):
    try:
        results = places.get_tourist_attractions_in_country(country_code)
        tourist_attractions = list(map(lambda place: place.toJson(), results))
        return tourist_attractions
    except Exception as e:
        print(f"error happened {e}")
    return []


app.register_blueprint(country_controller)
app.register_blueprint(currency_conv_controller)
app.register_blueprint(places_controller)

if __name__ == '__main__':
    app.run(debug=True)
