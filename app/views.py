from flask import Flask, render_template, request, url_for, jsonify
from flask_bootstrap import Bootstrap
from .methods import *



app = Flask(__name__)
Bootstrap(app)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')



# Initialize the extension



@app.route('/_add_datas')
def add_datas():
    place = request.args.get("place", default="Résidence Foyer Montpellieret", type=str)
    place = clean_entry(place)
    # Geocoding an address
    coord = geocoding(place)
    address = get_add(coord)
    text = some_words_about(place)


    return jsonify(#coordinates=coord,
                   address=address,
                   lat=coord[0],
                   lng=coord[1],
                   wikipedia=text)


@app.route('/')
@app.route('/home/')
def index():

    return render_template("home.html")



if __name__ == "__main__":
    app.run()
