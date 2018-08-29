from app.methods import *

from io import BytesIO
import json
from os import environ
#from config import *
GG_APP_ID=environ.get('GG_APP_ID')

###test pytest###
def test_function():
    assert ma_fonction_a_tester(1, 1) == 2

#### test API enable####

def call_ggeocode():
    #build url
    url_begin = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key="
    key = GG_APP_ID
    url = "{}{}".format(url_begin,key)
    rep = requests.get(url)
    return rep.status_code

def call_mediawiki():
    url = "https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json&formatversion=2"
    rep = requests.get(url)
    return rep.status_code

def test_call_ggeocode():
    assert call_ggeocode() == 200

def test_call_mediawiki():
    assert call_mediawiki() == 200


#test geocoding with monkeypatch
def test_apigg_return(monkeypatch):
    """to test geocoding without API request"""
    result = [{'types': ['locality', 'political'], 'formatted_address': 'Montpellier, France', 'place_id': 'ChIJsZ3dJQevthIRAuiUKHRWh60', 'address_components': [{'types': ['locality', 'political'], 'short_name': 'Montpellier', 'long_name': 'Montpellier'}, {'types': ['administrative_area_level_2', 'political'], 'short_name': 'Hérault', 'long_name': 'Hérault'}, {'types': ['administrative_area_level_1', 'political'], 'short_name': 'Occitanie', 'long_name': 'Occitanie'}, {'types': ['country', 'political'], 'short_name': 'FR', 'long_name': 'France'}], 'geometry': {'viewport': {'southwest': {'lat': 43.566744, 'lng': 3.807044}, 'northeast': {'lat': 43.6532999, 'lng': 3.941279}}, 'location_type': 'APPROXIMATE', 'bounds': {'southwest': {'lat': 43.566744, 'lng': 3.807044}, 'northeast': {'lat': 43.6532999, 'lng': 3.941279}}, 'location': {'lat': 43.610769, 'lng': 3.876716}}}]


    def mockreturn(one, two):
        return result

    monkeypatch.setattr(googlemaps.Client, 'geocode', mockreturn)
    place = ParsePlace("Montpellier")
    place.geocoding()
    assert place.lat == 43.610769
    assert place.lng == 3.876716
    assert place.address == 'Montpellier, France'



#test wikipedia with monkeypatch
class RequestResponse:
    def json(self):
        fake_json = [
        {
            "titre_album": "Abacab" ,
            "groupe": "Genesis" ,
            "annee": 1981 ,
            "genre": "Rock"
        }]
        return fake_json

def mafonction(url):
    return RequestResponse()

def test_call_wiki(monkeypatch):
    """to test wikipedia without API request"""
    place = "Montpellier"
    monkeypatch.setattr('app.methods.requests.get', mafonction)

    file = call_wiki_found_page(place)
    assert file == [
        {
            "titre_album": "Abacab" ,
            "groupe": "Genesis" ,
            "annee": 1981 ,
            "genre": "Rock"
        }]



####### Test Class ParsePlace ######
class TestParsePlace():

    place = ParsePlace("je veux aller à la piscine Antigone")

    def test_clean_entry(self):
        self.place.clean_entry()
        assert self.place.user_entry == "piscine Antigone"


    def test_place_for_ggapp(self):
        self.place.place_for_ggapp()
        assert self.place.user_entry == "piscine+Antigone"

    def test_geocoding(self):
        self.place.geocoding()
        assert self.place.lat == 43.6071353
        assert self.place.lng == 3.8930501
        assert self.place.address == "195 Avenue Jacques Cartier, 34000 Montpellier, France"

    def test_format_add(self, monkeypatch):
        answer_beginning = "Bravo! "

        def mockreturn(one):
            return answer_beginning

        monkeypatch.setattr(random, 'choice', mockreturn)
        self.place.format_add()
        assert self.place.address == "Bravo! 195 Avenue Jacques Cartier, 34000 Montpellier, France"


def test_some_word_about(monkeypatch):

    b = "Ceci est un test: "

    def mockreturn(one):
        return b

    monkeypatch.setattr(random,'choice', mockreturn)
    text = some_words_about("ganges")
    print(text)
    assert text == "Ceci est un test: Ganges (en occitan Gange) est une commune française "\
            "située dans le département de l'Hérault, en région Occitanie. "\
            "Chef-lieu du canton de Ganges, la commune est située au confluent de l’Hérault "\
            "avec le Rieutord. Ses habitants sont appelés les Gangeois."

