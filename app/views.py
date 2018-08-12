from flask import Flask, render_template, request, jsonify
from .methods import *

#from flask_googlemaps import GoogleMaps
#from flask_googlemaps import Map

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
#gmaps = googlemaps.Client(key=app.config['GG_APP_ID'])


# Initialize the extension

#GoogleMaps(app, key = app.config['GG_APP_ID'])


@app.route('/_add_datas')
def add_datas():
    place = request.args.get("place", "Résidence Foyer Montpellieret", type=str)
    # Geocoding an address
    coord = geocoding(place)
    address = get_add(coord)
    text = some_words_about(place)
    #mymap = Map(
    #    identifier = "map",
    #    lat = coord[0],
    #    lng = coord[1],
    #    markers = [(coord[0], coord[1])],
    #    zoom = 13)

    return jsonify(coordinates=coord,
                   address=address,
                   lat=coord[0],
                   lng=coord[1],
                   wikipedia=text)


@app.route('/')
@app.route('/home/')
def index():
    key = app.config['GG_APP_ID']  # to send api key to the call javascript result.html to display the map
    return render_template("home.html",
                           key=key)


if __name__ == "__main__":
    app.run()
