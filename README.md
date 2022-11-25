Projet MOTUS - Full Stack Data

Nous sommes trois étudiants de l'ESIEE Paris, Samy Abdouche, Mickael Mickaël Bannholtzer et Shayan Arnal.

Dans le cadre de ce projet de fin d'unité en Application Full Stack Data correspondant au créneau DSIA 5102A nous avons choisis de réaliser une réplique du cèlèbre jeu télévisé "MOTUS". 
Ce jeu n'étant plus diffusé à l'antenne depuis mai 2019 nous avons décidé de lui redonner vie avec ce projet qui nous permettra d'appliquer nos compétences acquises tout au long de l'unité.

Nous allons en effet réaliser le front en react et en javascript ainsi que le back framework en fast api et la base de donnée en post gre SQL.
La base de donnée utilisée se nomme "lexique" et provient du site http://www.lexique.org/ elle possède 140 000 mots de la langue française ce qui constitue la quasi totalité des mots de la langue française et leurs variantes.
L'accès à cette base de donnée sera effectué par appel d'API ce qui nous permet de ne pas avoir à la stocker.
Pour que le jeu soit accessible à tous nous allons nous concentrer sur les environs 10 000 mots utilisés le plus fréquemment. Nous pouvons pour cela sélectionner les mots de de frequence supérieur à 50 dans notre dataset (ce qui correspond à envrion 12 000 mots).
Nous allons également sélectionner uniquement les mots de 6 à 10 lettres. Nous pouvons également réaliser cette selection sur notre dataset et nous en avons environs 9000 dont la fréquence est supérieur à 50.

Pour synthétiser nous allons ici sélectionner les mots les plus fréquents (freq >50) dont le nombre de lettre est compris entre 6 et 10 lettres. Nous avons donc au total environ 9000 mots que nous allons proposer de deviner aux joueurs.

Nous allons configurer pour chaque joueur:

- Un identifiant de compte (unique) inconnu du joueur

- Nom

- Prénom

- Un surnom / nom d'utilisateur unique qui permet de référencer le joueur et de le référencer 

- Date de création de compte.

- Adresse mail, pour une éventuelle confirmation de création de compte et éventuelle récupération de mt de passe oublié

- Un mot de passe (haché) qui lui permettra d'accéder à son compte avec son nom d'utilisateur

- Un meilleur score actualisé à chaque partie










