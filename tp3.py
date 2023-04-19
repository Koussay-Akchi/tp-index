import os
import math
from ex3 import f1_stem, f5_poids, f4_calculer_idf
import operator
from collections import defaultdict

def lire_requete():
    requete = input("Veuillez saisir votre requête : ")
    return requete

def creer_fichier(requete):
    if not os.path.exists("requete"):
        os.mkdir("requete")
    f = open("requete/requete.txt", "w")
    f.write(requete)
    f.close()


def lire_fichier(nom_fichier):
    with open(nom_fichier, "r") as f:
        contenu = f.read()
    return contenu

def recherche_documents_pertinents(requete):
    creer_fichier(requete)
    poids_dict = f5_poids("documents")
    scores = {}
    
    mots_requete = f1_stem("requete/requete.txt")
    for mot in mots_requete:
        if mot in poids_dict:
            print(mot+" trouvé!")
            for doc, poids in poids_dict[mot].items():
                if doc not in scores:
                    scores[doc] = poids
                else:
                    scores[doc] += poids    
    sorted_docs = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

    print("Liste des documents pertinents pour la requête :"+requete)
    for doc, score in sorted_docs:
        print(doc+" (score: " + str(score) + " )")