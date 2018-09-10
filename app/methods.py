import googlemaps
import re
import requests
import random
from .const import *
from os import environ

gmaps = googlemaps.Client(key = environ.get('GG_APP_ID'))



#test pytest
def ma_fonction_a_tester(a, b):
    return a + b

#Api(s) google

class ParsePlace():


    def __init__(self, user_input):
        self.user_entry = user_input
        self.lat = None
        self.lng = None
        self.address = None

    def empty_input(self):
        """return some date when user tapes nothing"""
        self.lat = 45.950007
        self.long = 1.756338
        self.address = "{}{}".format(ANSWERWHENNOTHING[0], "21 Route de la Cascade, 23400 Bourganeuf")



    def clean_entry(self):
        '''clean user entry in order to push to API wikipedia'''
        words = self.user_entry.split()
        words_cleaned = [i for i in words if i not in STOPWORDS]
        entry = " ".join(words_cleaned)
        # remove the letter before the "'" character
        r = r".[']"
        self.user_entry = re.sub(r, "", entry)


    def place_for_ggapp(self):
        '''in order to give a correct entry for google "word+word"'''
        pl_list = self.user_entry.split()
        self.user_entry = "+".join(pl_list)


    def geocoding(self):
        """get geographical coordinates: latitude"""

        geocode_result = gmaps.geocode(self.user_entry)

        try:
            self.lat = geocode_result[0]["geometry"]["location"]["lat"]
            self.lng = geocode_result[0]["geometry"]["location"]["lng"]
            self.address = geocode_result[0]["formatted_address"]
        except IndexError:
        #to skip indexerror when a place is not find we put temporaly the coords of a nice place in France
            self.lat = 0
            self.lng = 0
            self.address ="No address found"


    def format_add(self):
        """get the place adress"""
        if self.address == "No address found":
            self.address = "Désolé je ne trouve pas d'adresse"
        else:
            answer_beginning = random.choice(ANSWERSADD)
            self.address = "{}{}".format(answer_beginning,self.address)

#Api Wikipedia
def call_wiki_main_page(place):
    """Call Api Wikipedia"""
    #first call all main page
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=&srsearch="
    url_title = place
    url = "{}{}".format(url_begin, url_title)
    #and we took the first occurrence
    response = requests.get(url)
    file = response.json()
    try:
        title = file["query"]["search"][0]["title"]
    except IndexError:
        title = "Citroën 2 CV"  # in case of invalid user input we put a default answer
    return title

def call_wiki_found_page(title):
    # format url
    url_begin = "https://fr.wikipedia.org/w/api.php?action=query&titles="
    url_title = title
    url_end = "&prop=extracts&exsentences=3&format=json&explaintext&exlimit=max&exintro"
    url = "{}{}{}".format(url_begin, url_title, url_end)

    # call api
    response = requests.get(url)
    file = response.json()
    return file

def some_words_about(place):
    """Extract and treat wikipedia contents"""
    page_title = call_wiki_main_page(place)
    article = call_wiki_found_page(page_title)

    try:
        a = article["query"]["pages"]
        # to skip pg id number witch differs from page to page
        for value in a.values():
            extract = value["extract"]
            # format GPY answer
            b = random.choice(ANSWERSSTORY)
            text = "{}{}".format(b, extract)

            #add a mock answer when the page is not found
            for k,v in a.items():
                if k == "85296": #the page id of "2CV"
                    text = "{}\n{}".format(ANSWERWHERENOIDEA[0], extract)


    except IndexError:
        text = "Verifie ton orthographe pour avoir une histoire ! En attendant je parle dans ma barbe !!!"

    return text



def some_words_about_whith_nothing():
    """when the user tape nothing """
    response = requests.get('https://fr.wikipedia.org/w/api.php?action=query&titles=P%C3%A9tanque&prop=extracts&exsentences=3&format=json&explaintext&exlimit=max&exintro')
    file = response.json()
    a = file["query"]["pages"]
    # to skip pg id number witch differs from page to page
    for value in a.values():
        extract = value["extract"]
        # format GPY answer
        b = ANSWERWHENNOPLACE[0]
        text = "{}{}".format(b, extract)
    return text




