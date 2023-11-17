from flask import render_template, redirect, url_for
from app import app, db
from app.models import City, Country, CityTime
from app.forms import CityTimeForm, CountryDetailsForm, CityDetailsForm
import requests
import time


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/city_time", methods=["GET", "POST"])
def city_time():
    form = CityTimeForm()

    if form.validate_on_submit():
        city_id = form.cityID.data

        url = ("https://wft-geo-db.p.rapidapi.com/v1/geo/cities/1/time")

        headers = {
            "X-RapidAPI-Key": "3f1b81d470msh7ae4427a11dc855p166491jsnf9b1fea50b87",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        # print(response_json)

        if response_json:
            cityID = city_id
            cityTime = response_json["data"]


            citytime = CityTime(
                cityID=cityID,
                cityTime=cityTime
            )

            db.session.add(citytime)
            db.session.commit()

            form.cityID.data = ""

        return render_template("display_city_time.html", response_json=response_json, city_id=city_id)

    return render_template("city_time.html", form=form)


@app.route("/city_details", methods=["GET", "POST"])
def city_details():
    form = CityDetailsForm()

    if form.validate_on_submit():
        city_id = form.cityID.data

        url = ("https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + city_id)

        headers = {
            "X-RapidAPI-Key": "3f1b81d470msh7ae4427a11dc855p166491jsnf9b1fea50b87",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        if response_json["data"]:
            name = response_json["data"]["name"]
            population = response_json["data"]["population"]
            country = response_json["data"]["country"]

            citydetails = City(
                name=name, population=population, country=country
            )

            db.session.add(citydetails)
            db.session.commit()

            form.cityID.data = ""

        return render_template("display_city_details.html", response_json=response_json, city_id=city_id, name=name, population=population, country=country)

    return render_template("city_details.html", form=form)


@app.route("/country_details", methods=["GET", "POST"])
def country_details():
    form = CountryDetailsForm()

    if form.validate_on_submit():
        country_id = form.countryID.data

        url = ("https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country_id)

        headers = {
            "X-RapidAPI-Key": "3f1b81d470msh7ae4427a11dc855p166491jsnf9b1fea50b87",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        if response_json["data"]:
            name = response_json["data"]["name"]
            capital = response_json["data"]["capital"]
            callingCode = response_json["data"]["callingCode"]
            numRegions = response_json["data"]["numRegions"]

            country = Country(
                name=name, capital=capital, callingCode=callingCode, numRegions=numRegions
            )

            db.session.add(country)
            db.session.commit()

            form.countryID.data = ""

        return render_template("display_country_details.html", response_json=response_json, country_id=country_id, name=name, capital=capital, callingCode=callingCode, numRegions=numRegions)

    return render_template("country_details.html", form=form)