## COMMENT CORRECTEMENT PROCÉDER SUR GIT

Le point principal est le suivant : ON NE TOUCHERA JAMAIS À LA BRANCHE MASTER. À chaque étape de développement, il faudra créer une branche à partir de master.

Une fois vos traitements effectués, il faudra push la branche en question sur le repo distant, faire un git pull sur master (pour récupérer les dernières modifications apportées à la branche principale), puis merge la branche que vous avez poussée dans le master, et on réitère le processus.
