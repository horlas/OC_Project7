import googlemaps
import re
import requests
import random
from .const import *

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
    a = reverse_geocode_result[0]["formatted_address"]
    b = random.choice(ANSWERSADD)
    res = "{}{}".format(b,a)
    return res # type: str

#Treatment of user entry
########################################################################
#def extract_own_name(place):
#    """to extract only the own name"""
#    c_name = r"\b[a-z]*"
#    own_name = r"[A-Z][a-z]*"
#    place = re.sub(c_name,"",place)
#    return place


def clean_entry(place):
    # clean user entry in order to push to API wikipedia

    words = place.split()
    words_cleaned = [i for i in words if i not in STOPWORDS]
    entry = " ".join(words_cleaned)
    #remove the letter before the "'" character
    r =r".[']"
    entry = re.sub(r,"",entry)
    print(entry)
    return entry

def place_for_ggapp(place_gg):
    '''in order to give a correct entry for google "word+word"'''
    place = place_gg.split()
    entry = "+".join(place)
    print(entry)
    return entry





def test_empty_entry(file):
    """to ensure that the page required is not empty"""
    k = False
    try:
        a = file["query"]["pages"][0]
        for i in a.keys():
            if i == "missing":
                k = a['missing']
            elif i == "invalid":
                k = a['invalid']

    except KeyError:
        print("no wikipedia page found")
        k = True
        return k

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
    #first call all main page
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=&srsearch="
    url_title = place
    url = "{}{}".format(url_begin, url_title)
    print(url)
    #and we took the first occurrence
    response = requests.get(url)
    file = response.json()
    try:
        place = file["query"]["search"][0]["title"]
    except IndexError:
        place = "Coq"

    # format url
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&titles="
    url_title = place
    url_end = "&prop=extracts&exsentences=3&format=json&explaintext"
    url = "{}{}{}".format(url_begin, url_title, url_end)

    # call api
    print(url)
    response = requests.get(url)
    file = response.json()

    #format GPY answer
    #b = random.choice(ANSWERSSTORY)
    #res = "{}{}".format(b, file)
    #if place == "Coq":
    #    res = "{}{}".format(ANSWERWHERENOIDEA, file)

    return file



def some_words_about(place):
    """Extract and treat wikipedia contents"""
    file = call_wiki(place)
    print(file)
    try:
        a = file["query"]["pages"]
        dict = {}
        # to skip pg id number witch differs form page to page
        for value in a.values():
            dict = value
            text = dict["extract"]
        return text

    except IndexError:
        print("no page found XXXX")
        text = "Verifie ton orthographe pour avoir une histoire ! En attendant je bloblote du cerveau!!"

    return text


def some_words_about_v2(place):
    """Use wikipedia geocoding"""




