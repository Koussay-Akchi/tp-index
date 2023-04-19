import os

def f1_stem(val):
    stop_list = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
    f = open(val, "r")
    mots = f.read().split()
    mots= [mots.lower() for mots in mots if mots not in stop_list]

    import re
    mots=[mots for mots in mots if re.match(r"^[a-z]+$", mots)]

    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    [stemmer.stem(mots) for mots in mots]

    f.close()

    sortie=open("sortie_f1.txt", "w")
    for i in mots:
        sortie.write(i+" ")
    sortie.close()
    f = open("sortie_f1.txt", "r")
    mots2 = f.read().split()
    f.close()
    return(mots2)


def f2_dict(val):
    f = open(val, "r")
    mots = f.read().split()
    long=len(mots)
    i = 0
    dict = {}
    while i < long:
        word=mots[i]
        dict[mots[i]] = mots.count(word)
        i += 1
    f.close()
    return(dict)    

def f3_global(dossier_g):
    dict_global={}
    for fichier in os.listdir(dossier_g):
        dict_global.update(f2_dict(dossier_g+"/"+fichier))
    print(dict_global)
    return(dict_global)

def f4_calculer_idf(dossier_g):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    idf_dict = {}

    for fichier in os.listdir(dossier_g):
        chemin=dossier_g+"/"+fichier
        mots =f1_stem(chemin) 
        for mot in mots:
            if mot not in idf_dict:
                idf_dict[mot] = 1
            else:
                idf_dict[mot] += 1

    return idf_dict

def f5_poids(dossier_g):
    poids_dict = {}
    idf=f4_calculer_idf(dossier_g)
    for fichier in os.listdir(dossier_g):
        chemin=dossier_g+"/"+fichier
        mots = f1_stem(chemin)
        for mot in mots:
            tf = mots.count(mot) / len(mots)
            poids = tf * idf.get(mot, 0)
            if mot not in poids_dict:
                poids_dict[mot] = {fichier: poids}
            else:
                poids_dict[mot][fichier] = poids
    with open("sortie_f5.txt", "w") as f:
        for mot, poids in poids_dict.items():
            f.write(mot + ": " + str(poids) + "\n")
    return poids_dict

def f6_fich_inv(dossier_g):
    dict_global = f3_global(dossier_g)
    poids_dict = f5_poids(dossier_g)
    with open("fich-inv.txt", "w") as f:
        for stem in dict_global:
            f.write("======= "+stem+" =========\n")
            for doc, poids in poids_dict.get(stem.lower(), {}).items():
                f.write(stem+"-----"+doc+"-----"+ str(poids) + "\n")