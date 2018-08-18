import googlemaps
import re
import requests
import random
from .const import *

from config import *

from stop_words import get_stop_words


gmaps = googlemaps.Client(key = GG_APP_ID)



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

    def clean_entry(self):
        # clean user entry in order to push to API wikipedia

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
            b = random.choice(ANSWERSADD)
            self.address = "{}{}".format(b,self.address)





#Treatment of user entry
########################################################################
#def extract_own_name(place):
#    """to extract only the own name"""
#    c_name = r"\b[a-z]*"
#    own_name = r"[A-Z][a-z]*"
#    place = re.sub(c_name,"",place)
#    return place










#def test_empty_entry(file):
#    """to ensure that the page required is not empty"""
#    k = False
#    try:
#        a = file["query"]["pages"][0]
#        for i in a.keys():
#            if i == "missing":
#                k = a['missing']
#            elif i == "invalid":
#                k = a['invalid']

#    except KeyError:
#        print("no wikipedia page found")
#        k = True
#        return k

#    return k

#def extract_text(file):
#    """to extract content of wikipedia and treat it"""
#    text = file["query"]["pages"][0]["extract"]
#    bal_html = r"<.*?>"
#    century = r"&#160;"
#    text = re.sub(bal_html,r"",text)
#    text = re.sub(century,r"ème ",text)
#    return text


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



    return file



def some_words_about(place):
    """Extract and treat wikipedia contents"""
    file = call_wiki(place)
    print(file)
    try:
        a = file["query"]["pages"]
        # to skip pg id number witch differs from page to page
        for value in a.values():
            extract = value["extract"]
            # format GPY answer
            b = random.choice(ANSWERSSTORY)
            text = "{}{}".format(b, extract)

            #add a mock answer when the page is not found
            for k,v in a.items():
                if k == "1815754": #the page id of "Coq"
                    text = "{}\n{}".format(ANSWERWHERENOIDEA[0], extract)


    except IndexError:
        print("no page found XXXX")
        text = "Verifie ton orthographe pour avoir une histoire ! En attendant je bloblote du cerveau!!"

    return text


def some_words_about_v2(place):
    """Use wikipedia geocoding"""





