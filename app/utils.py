from stop_words import get_stop_words
import re

def extract_add(reverse_geocode_result):
    """to extract address from the result of google api reverse geocoding"""
    a = reverse_geocode_result[0]
    return a["formatted_address"]


#Treatment of user entry
########################################################################
def extract_own_name(place):
    """to extract only the own name"""
    c_name = r"\b[a-z]*"
    own_name = r"[A-Z][a-z]*"
    place = re.sub(c_name,"",place)
    return place


def clean_entry(place):
    """clean entry in order to push to API wikipedia"""
    stop_words = get_stop_words("fr")
    words = place.split()
    words_cleaned = [i for i in words if i not in stop_words]
    return " ".join(words_cleaned)


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




