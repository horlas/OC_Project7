# -*-coding:utf-8 -

from stop_words import get_stop_words

#This file contains Grand Py vocabulary

ANSWERSADD = [

    "Biensur mon poussin, la voici :    ",
    "Mais rien ne me fait plus plaisir que de te la donner :   ",
    "Comment puis je à mon age connaitre encore tout ça ! La voici :    ",
    "Oh regarde! La jolie adresse ! :   ",
    "Tu veux pas aller voir ta grand-mère ? :    "

]


ANSWERSSTORY = [

    "Et t'ai je déjà raconté cette histoire ? :\n          ",
    "Je me souviens que ....\n        ",
    "Si tu as cinq minutes , je te raconte une petite histoire ! :\n        ",
    "De mon temps ....\n",
    "Je profite d'avoir un peu de compagnie pour papoter !\n      "
]

ANSWERWHERENOIDEA = [
    "Fais attention à l'orthographe de ta recherche. Mais en attendant je peux te parler de ma première voiture: la 2CV. "

]

ANSWERWHENNOTHING = ["Ben alors ! Tu ne  veux pas parler ? Je te donne mon adresse alors ! " ]
ANSWERWHENNOPLACE = ["Ben alors ! Si tu ne veux pas parler veux tu que je te parle du jeu que je prefère ! "]


#STOP_WORDS

ADDSTOPWORDS = ['Salut', 'GrandPy', '!', 'Est-ce', 'que', 'tu', 'connais', "l'adresse ", "d'", '?', "je", "Je","veux", "aller"]
STOPWORDS = get_stop_words("fr")
for i in ADDSTOPWORDS:
    STOPWORDS.append(i)
