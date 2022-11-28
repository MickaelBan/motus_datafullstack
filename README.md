Projet MOTUS - Full Stack Data

Nous sommes trois étudiants de l'ESIEE Paris, Samy Abdouche, Mickaël Bannholtzer et Shayan Arnal.

Dans le cadre de ce projet de fin d'unité en Application Full Stack Data correspondant au créneau DSIA 5102A nous avons choisis de réaliser une réplique du cèlèbre jeu télévisé "MOTUS". 
Ce jeu n'étant plus diffusé à l'antenne depuis mai 2019 nous avons décidé de lui redonner vie avec ce projet qui nous permettra d'appliquer nos compétences acquises tout au long de l'unité.

Nous allons en effet réaliser le front en react et en javascript ainsi que le back framework en fast api et la base de donnée en post gres SQL.
La base de donnée utilisée se nomme "lexique" et provient du site http://www.lexique.org/ elle possède 140 000 mots de la langue française ce qui constitue la quasi totalité des mots de la langue française et leurs variantes.
L'accès à cette base de donnée sera effectué par appel d'API ce qui nous permet de ne pas avoir à la stocker.

Nous allons configurer pour chaque joueur:

- Un identifiant de compte (unique) inconnu du joueur

- Nom

- Prénom

- Un surnom / nom d'utilisateur unique qui permet de référencer le joueur et de le référencer 

- Date de création de compte.

- Adresse mail, pour une éventuelle confirmation de création de compte et éventuelle récupération de mot de passe oublié

- Un mot de passe (haché) qui lui permettra d'accéder à son compte avec son nom d'utilisateur

- Un meilleur score actualisé à chaque partie










