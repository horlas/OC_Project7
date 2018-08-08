from flask import Flask, render_template, request
import googlemaps
import requests
from .utils import *
from .models import *


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
gmaps = googlemaps.Client(key = app.config['GG_APP_ID'])


# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/')
@app.route('/result/')
def result():
    place = request.args.get("place")
    # Geocoding an address
    coord = geocoding(place)
    address = get_add(coord)

    key = app.config['GG_APP_ID'] #to send api key to the call javascript result.html to display the map

    text = some_words_about(place)

    return render_template("result.html",
                           coordinates = coord,
                           latitude = coord[0],
                           longitude = coord[1],
                           adresse = address,
                           wikipedia = text,
                           key = key)



if __name__ == "__main__":
    app.run()
