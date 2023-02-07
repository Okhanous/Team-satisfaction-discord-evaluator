import json
import statistics

from numpy import append

def indic_categorie_personne(categorie, personne):

    dict_remplir = {}

    with open('test.json') as json_file:
            dict_remplir = json.load(json_file)

    liste_resultat = []
    for dict_date in dict_remplir.values():
            if personne in dict_remplir["0"].keys() :
                liste_resultat.append(dict_date[personne][categorie])

    return liste_resultat

def indic_categorie_mean(categorie, personnes):
        all_values_for_categorie = []
        mean_values_for_categorie = []
        dict_remplir = {}

        with open('test.json') as json_file:
                        dict_remplir = json.load(json_file)

        for i in get_semaines():
                all_values_for_categorie = []
                for personne in personnes :
                        all_values_for_categorie.append(dict_remplir[i][personne][categorie])
                mean_values_for_categorie.append(statistics.mean(all_values_for_categorie))
        return mean_values_for_categorie
        


def get_semaines():

    dict_remplir = {}

    with open('test.json') as json_file:
            dict_remplir = json.load(json_file)

    return list(dict_remplir.keys())
