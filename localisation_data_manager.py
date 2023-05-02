import json
from os import path
from datetime import date, timedelta


def load_json_data_from_file(filename):
    f = open(filename, "r")
    json_data = f.read()
    f.close()
    return json_data


def save_cleaned_data_to_file(filename, city_data):
    json_data = json.dumps(city_data)
    f = open("clean_"+filename, "w")
    f.write(json_data)
    f.close()


def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def constructeur_clean_localisation_json_file(filename):
    # le fichier json existe
    if path.exists(filename):
        localisations_json = load_json_data_from_file(filename)
        localisations = json.loads(localisations_json)

    # creation d'une liste de données exploitables
    localisation_sans_underscore = []
    for donnees in localisations:
        donnees_replace = donnees[0].replace("_", " ")
        donnees_nettoyees = donnees_replace.split(" ")
        localisation_sans_underscore.append(donnees_nettoyees)
    # sauvegarde de la nouvelle liste dans nouveau fichier json
    save_cleaned_data_to_file(filename, localisation_sans_underscore)

    return localisation_sans_underscore

# liste_clean = []
# for localisation in localisation_sans_underscore:
#     for loc in localisation:
#         is_float(loc)
#         liste
# print(localisation_sans_underscore)


def api_url_construteur(ville_cible, date_prevision):
    FILENAME = "localisation.json"
    site = "https://api.open-meteo.com/v1/forecast?"
    liste_localisations_clean = constructeur_clean_localisation_json_file(FILENAME)
    # ville_cible = 'Paris'
    latitude = ""
    longitude = ""
    for localisations in liste_localisations_clean:
        if ville_cible in localisations:
            latitude = localisations[-3]
            longitude = localisations[-2]
            city = "latitude=" + latitude + "&longitude=" + longitude
    date_start = date.today().strftime("%Y-%m-%d")
    d_prevision = date.today() + timedelta(date_prevision)
    date_end = d_prevision.strftime("%Y-%m-%d")

    url_complete = site + city + "&hourly=temperature_2m&" \
                                "forecast_days=1&start_date="+ date_start +"&end_date="+ date_end +"&timezone=Europe%2FLondon"
    return url_complete

