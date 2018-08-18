from .methods import *
import pytest
from config import *
import requests

##### tester les API####


def call_ggeocode():
    #build url
    url_begin = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="
    key = GG_APP_ID
    url = "{}{}".format(url_begin,key)
    rep = requests.get(url)
    return rep.status_code

def call_wiki():
    url = "https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json&formatversion=2"
    rep = requests.get(url)
    return rep.status_code

def test_call_ggeocode():
    assert call_ggeocode() == 200

def test_call_mediawiki():
    assert call_wiki() == 200



def test_function():
    assert ma_fonction_a_tester(1, 1) == 2

@pytest.fixture
def exemple_place():
    place = "Opera+Comedie"
    return place

def test_geocoding(exemple_place):
    assert geocoding(exemple_place) == (43.6078257, 3.8786943)




