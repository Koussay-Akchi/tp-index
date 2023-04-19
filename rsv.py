import math
from ex3 import f1_stem, f5_poids, f4_calculer_idf
from collections import defaultdict

def rsv(dossier_g):
    requete_stemmed = f1_stem("requete/requete.txt")
    poids_dict = f5_poids(dossier_g)
    idf_dict = f4_calculer_idf(dossier_g)
    scores = defaultdict(float)
    for mot in requete_stemmed:
        if mot in poids_dict:
            tf_requete = requete_stemmed.count(mot) / len(requete_stemmed)
            idf = math.log(len(poids_dict) / idf_dict.get(mot, 1))
            for doc, tf_doc in poids_dict[mot].items():
                scores[doc] += tf_requete * tf_doc * idf
    sorted_docs = sorted(scores.items())
    return sorted_docs
