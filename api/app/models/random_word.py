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


#prog du jeux:


word_input = input("please enter your word: ")
word_check = ""

while word_input != word_check:
    
    word_input = input("enter a word: ")
    copy_word_input = word_input
    word = "xxxxxx"
    copy_word_check = word_check
    
    for i in range (6):
        if copy_word_input[i] == copy_word_check[i]:
        
            word = word[:i] + copy_word_check[i].upper() + word[i+1:]
        
            copy_word_input = copy_word_input[:i]+"@"+copy_word_input[i+1]
        
            copy_word_check = copy_word_check[:i]+"!"+copy_word_check[i+1:]
        
    for i in range (6):
        if copy_word_check[i] == copy_word_input[i]:
        
            word = word[:i] + copy_word_check[i] + word[i+1:]
        
            ii = copy_word_input.find(copy_word_check[i])
        
            copy_word_input = copy_word_input[:ii]+"@"+copy_word_input[ii+1]
        
        elif word[i] == "x":
        
            word = word[:i] + "." + word[i+1:]
            
    print("your word: ",word_check, "the word you had to guess: ",word)
