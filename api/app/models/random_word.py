#Je vous mets ici un petit code pour permettre de prendre un mot au hasard dans une database :


import requests
import random

word_site = "https://www.XXXXXXXXXX"

# Il faudra ici mettre le lien qui accède à notre database nettoyé avec les mots entre 6 et 10 lettres 
# et aussi qui apparaissent le plus fréquemmement

# le lien de la database est la : http://www.lexique.org/



response = requests.get(word_site)
WORDS = response.content.splitlines()

word = random.choice(WORDS)
print(word)


# ça nous renvoie un mot au hasard de la liste c'est la façon la plus simple que j'ai trouvée mais il y en a d'autre


