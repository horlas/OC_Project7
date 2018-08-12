import googlemaps
import re
import requests

from config import *

from stop_words import get_stop_words


gmaps = googlemaps.Client(key = GG_APP_ID)

#Api(s) google

def geocoding(place):
    """get geographical coordinates: latitude"""

    geocode_result = gmaps.geocode(place)

    if geocode_result != []:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
    else:
        #to skip indexerror when a place is not find we put temporaly the coords of a nice place in France
        lat = 45.954243
        lng = 1.758278
    coord = (lat, lng)
    return coord

def get_add(coord):
    """get the place adress"""
    reverse_geocode_result = gmaps.reverse_geocode(coord)

    #a = extract_add(reverse_geocode_result)
    a = reverse_geocode_result[0]["formatted_address"]
    return a # type: str

#Treatment of user entry
########################################################################
def extract_own_name(place):
    """to extract only the own name"""
    c_name = r"\b[a-z]*"
    own_name = r"[A-Z][a-z]*"
    place = re.sub(c_name,"",place)
    return place


#def clean_entry(place):
#    """clean entry in order to push to API wikipedia"""
#    stop_words = get_stop_words("fr")
#    words = place.split()
#    words_cleaned = [i for i in words if i not in stop_words]
#    return " ".join(words_cleaned)


def test_empty_entry(file):
    """to ensure that the page required is not empty"""
    k = False
    a = file["query"]["pages"][0]
    for i in a.keys():
        if i == "missing":
            k = a['missing']

    return k

def extract_text(file):
    """to extract content of wikipedia and treat it"""
    text = file["query"]["pages"][0]["extract"]
    bal_html = r"<.*?>"
    century = r"&#160;"
    text = re.sub(bal_html,r"",text)
    text = re.sub(century,r"ème ",text)
    return text


#Api Wikipedia
def call_wiki(place):
    """Call Api Wikipedia"""

    #entry = clean_entry(place)

    #clean user entry in order to push to API wikipedia
    stop_words = get_stop_words("fr")
    words = place.split()
    words_cleaned = [i for i in words if i not in stop_words]
    entry = " ".join(words_cleaned)



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
    """Extract and treat wikipedia contents"""
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



