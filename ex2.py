stop_list = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]
f = open("fich-test.txt", "r")
mots = f.read().split()
mots= [mots.lower() for mots in mots if mots not in stop_list]

import re
mots=[mots for mots in mots if re.match(r"^[a-z]+$", mots)]

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
[stemmer.stem(mots) for mots in mots]

f.close()

sortie=open("sortie.txt", "w")
for i in mots:
    sortie.write(i+" ")
sortie.close()