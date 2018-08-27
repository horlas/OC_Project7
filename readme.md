#GrandPy Robot 


Grandpy Robot est un robot qui invite l'utilisateur à demander l'adresse d'un endroit où il aimerait aller. Suite à la demande , il le  renseigne en lui renvoyant l'adresse  et la carte du lieu demandé ,et une brève histoire en rapport avec cet endroit.

 Les phrases de GrandPy Robot peuvent être rigolotes par moment . Lorsqu'il ne trouve pas l'adresse c'est que l'utilisatteur a fait une mauvaise saisie , le robot parle alors de la première voiture qu'il a posédé : la 2CV ;-) !


L'application Grandpy Robot a été dévollopée dans le cadre du **Projet 7** du **parcours Python OpenclassRooms**.
Elle est devellopée en langage python et utilise le micro Framework **Flask**.

Pour satisfaire les fonctionnalités de Grandpy Robot, l'application fait deux appels simultanés aux API Google et Wikipédia. 

Vous pouvez consulter l'application sur **Heroku** : 
https://papyrobotag.herokuapp.com/

Pour installer l'application Grandpy Robot sur votre ordinateur:
Pour cela il est necessaire d'obtenir auprés de Google API une clé pour les API suivantes: geocoding API, Maps Javascript API:
 https://developers.google.com/maps/documentation/geocoding/get-api-key

Sous linux : creer le dossier qui contiendra l'application:
```
mkdir MonDossier
```
Se placer dans le dossier 
```
cd MonDossier
```
Creer un dépot git : 
```
MonDossier$ git init
```
Installer pip:
```
MonDossier$ sudo apt install python3-pip
``` 
Installer virutualenv :

```
MonDossier$  python3 -m pip install --user virtualenv
```
Creer un environnement virtuel sous le dossier: 


```
MonDossier$ python3 -m virtualenv venv
```
 
 Activer l'environnement virtuel : 
 
```
MonDossier$ source venv/bin/activate
```
Installer le dépôt distant de l'application: 
```
(venv)MonDossier$ git pull https://github.com/horlas/OC_Project7.git 
```
Installer les dépendances nécessaires à l'application: 
```
(venv)MonDossier$ pip install  -r requirements.txt
```
Instancier votre clé d'API Google en tant que variable d'environnement dans la console sous l'environnement virtuel toujours actif **(Attention cette variable doit s'appeler impérativement GG_APP_ID)**
```
(venv)MonDossier$ export GG_APP_ID=Votre_clé_d'API
```
Vous pouvez verifier qu'elle soit bien instanciée avec la commande suivante: 
```
printenv GG_APP_ID
```

Lancer l'application : 
```
(venv)MonDossier$ python run.py
```
Ouvrez l'application web en local : 127.0.0.1:5000.

Enjoy !!!




#GrandPy Robot

Grandpy Robot is a robot that invites the user to ask the address of a place where he would like to go. Following the request, he informs him by sending him the address and the map of the place requested, and a brief history related to this place.

GrandPy Robot's sentences can be funny at times. When he does not find the address is that the user has made a bad entry, the robot then speaks of the first car he has posed: the 2CV ;-)

The Grandpy Robot App has been devoloped as part of ** Project 7 ** ** Python OpenclassRooms **.
It is develloped in python language and uses the Micro Framework ** Flask **.

You can view the application on ** Heroku **:
https://papyrobotag.herokuapp.com/

To install the Grandpy Robot app on your computer:
For this it is necessary to obtain from Google API a key for the following APIs: geocoding API, Maps Javascript API:
 https://developers.google.com/maps/documentation/geocoding/get-api-key
											
Under linux: create the folder that will contain the application:
```
mkdir MonDossier
```
Under this folder....
```
cd MonDossier
```
Create a git repository : 
```
MonDossier$ git init
```
Install pip:
```
MonDossier$ sudo apt install python3-pip
``` 
Install virutualenv :

```
MonDossier$  python3 -m pip install --user virtualenv
```
Create a virtual environnement

```
MonDossier$ python3 -m virtualenv venv
```
 
Activate the virtual environnement
 
```
MonDossier$ source venv/bin/activate
```
Install the repository of the application: 
```
(venv)MonDossier$ git pull https://github.com/horlas/OC_Project7.git 
```
Install dependencies needed for the application: 
```
(venv)MonDossier$ pip install  -r requirements.txt
```
Instantiate your Google API key as an environment variable in the console under the always active virtual environment ** (Attention this variable must be imperatively called GG_APP_ID) ***
```
(venv)MonDossier$ export GG_APP_ID=Votre_clé_d'API
```
You can check that it is instantiated with the following command: 
```
printenv GG_APP_ID
```
Launch the application : 
```
(venv)MonDossier$ python run.py
```
Open localy the application : 127.0.0.1:5000.

Enjoy !!!
											
											
											
								