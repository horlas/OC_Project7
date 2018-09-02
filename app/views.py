from flask import Flask, render_template, request, url_for, jsonify
from flask_bootstrap import Bootstrap
from .methods import *
from os import environ

app = Flask(__name__)
Bootstrap(app)
# Config options - Make sure you created a 'config.py' file.
app.config['GG_APP_ID'] = environ.get('GG_APP_ID')


@app.route('/_add_datas')
def add_datas():
    user_input = request.args.get("place", type=str)
    place = ParsePlace(user_input)
    if user_input == "":
        place.empty_input()
        text = some_words_about_whith_nothing()
    else:
        place.clean_entry()
        place.place_for_ggapp()
        text = some_words_about(place.user_entry)
        place.geocoding()
        place.format_add()

    return jsonify(address = place.address,
                   lat = place.lat,
                   lng = place.lng,
                   wikipedia = text)


@app.route('/')
@app.route('/home/')
def index():
    return render_template("home.html")



if __name__ == "__main__":
    app.run()
