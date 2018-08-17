# -*-coding:utf-8 -

from stop_words import get_stop_words

#This file contains Grand Py vocabulary

ANSWERSADD = [

    "Biensur mon poussin, la voici :",
    "Mais rien ne me fait plus plaisir que de te la donner:",
    "Comment puis je à mon age connaitre encore tout ça ! La voici :",
    "Oh regarde! La jolie adresse!:",
    "Tu veux pas aller voir ta grand-mère ?"

]


ANSWERSSTORY = [

    "Et ai je déjà raconté cette histoire?:\n ",
    "Je me souviens que ....\n",
    "Si tu as cinq minutes , je te raconte une petite histoire!:\n",
    "De mon temps ....\n",
    "Je profite d'avoir un peu de compagnie pour te prendre la tete avec une histoire à deux balles!\n"
]

ANSWERWHERENOIDEA = [
    "Quand je te dis ça c'est que je n'ai pas trouvé d'histoire pertinente à raconter sur le sujet! \n"
]




#STOP_WORDS

ADDSTOPWORDS = ['Salut', 'GrandPy', '!', 'Est-ce', 'que', 'tu', 'connais', "l'adresse ", "d'", '?', "je", "Je","veux", "aller"]
STOPWORDS = get_stop_words("fr")
for i in ADDSTOPWORDS:
    STOPWORDS.append(i)
