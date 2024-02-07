from flask import Flask, request, Blueprint, make_response
import src.handler.CountryDataHandler as country_handler
import src.handler.CurrencyConverterDataHandler as currency_handler
import src.handler.SearchPlacesDataHandler as places

app = Flask(__name__)
# CORS(app, origins=["http://localhost:4200/"])

country_controller = Blueprint("country", __name__, url_prefix="/country")
currency_conv_controller = Blueprint("currency", __name__, url_prefix="/currency")
places_controller = Blueprint("places", __name__, url_prefix="/places")


@country_controller.get("/")
def hello_world():
    return "<p>Hello, World! I NEED TO MAKE 7 ENDPOINTS</p>"


@country_controller.get("/all")
def get_all_country_names():
    try:
        result = country_handler.get_all_country_names()
        jj = list(map(lambda country: country.toJson(), result))
        response = make_response(jj)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(f"something wrong happened {e}")
    return []


@country_controller.get("/capital/<country_code>")
def get_capital_city_by_country_name(country_code: str):
    try:
        result = country_handler.get_capital_city_by_cc(country_code)
        return result
    except Exception as e:
        print(e)
    return []


@country_controller.get("/profile/<country_code>")
def get_country_profile(country_code: str):
    try:
        result = country_handler.get_country_profile(country_code)
        response = make_response(result.toJson())
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
    return []


@country_controller.get("/currency/<country_code>")
def get_currency_code_by_country_code(country_code: str):
    try:
        result = country_handler.get_currency_code_by_cc(country_code)
        return result
    except Exception as e:
        print(e)
    return []


@currency_conv_controller.get("/convert")
def convert_currency():
    try:
        from_currency: str = request.args.get("from_currency", "us")
        to_currency: str = request.args.get("to_currency", "eur")
        amount: float = request.args.get("amount", 100)
        result = currency_handler.convert_currency(from_currency, to_currency, amount)

        response = make_response(result)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(f"error happened {e}")
    return None


@places_controller.get("/restaurants/<country_code>")
def get_restaurants_in_country(country_code: str):
    try:
        results = places.get_restaurants_in_country(country_code)
        restaurants = list(map(lambda place: place.toJson(), results))

        response = make_response(restaurants)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(f"error happened {e}")
    return []


@places_controller.get("/tourist/<country_code>")
def get_tourist_attractions_in_country(country_code: str):
    try:
        results = places.get_tourist_attractions_in_country(country_code)
        tourist_attractions = list(map(lambda place: place.toJson(), results))

        response = make_response(tourist_attractions)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(f"error happened {e}")
    return []


app.register_blueprint(country_controller)
app.register_blueprint(currency_conv_controller)
app.register_blueprint(places_controller)

if __name__ == '__main__':
    app.run(debug=True)
