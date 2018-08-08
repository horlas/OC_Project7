import googlemaps

import requests
from .utils import *
from config import *

gmaps = googlemaps.Client(key = GG_APP_ID)


#Api(s) google

def geocoding(place):
    """get geographical coordinates: latitude"""

    geocode_result = gmaps.geocode(place)

    if geocode_result != []:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
    else:
        #to skip indexerror when a place is not find we put temporaly the coords of a noce place in France
        lat = 45.954243
        lng = 1.758278
    coord = (lat, lng)
    return coord

def get_add(coord):
    """get the place adress"""
    reverse_geocode_result = gmaps.reverse_geocode(coord)
    a = extract_add(reverse_geocode_result)
    return a # type: str


#Api Wikipedia
def call_wiki(place):
    """Call Api Wikipedia"""

    entry = clean_entry(place)

    # format url
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&titles="
    url_title = entry
    url_end = "&redirects&prop=extracts&format=json&formatversion=2&exsentences=3"
    url = "{}{}{}".format(url_begin, url_title, url_end)

    # call api
    response = requests.get(url)
    file = response.json()
    return file


def some_words_about(place):
    file = call_wiki(place)
    test = test_empty_entry(file)
    if test is True:
        place = extract_own_name(place)
        file = call_wiki(place)
        test = test_empty_entry(file)
        if test is True:
            text = "Oups page non trouvée"
        else:
            text = extract_text(file)
    else:
        text = extract_text(file)
    return text