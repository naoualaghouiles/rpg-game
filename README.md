# cli-game

Squelette du projet de jeu RPG

L'idée est d'implémenter plusieurs actions que l'on pourrait retrouver dans un RPG.
Celles-ci seront réalisée au travers d'une classe `Game` et votre objectif final sera de rendre votre jeu accessible au travers d'une CLI.
Etant donné que vos actions doivent influer sur la partie et vos actions future, vous devrez stocker l'état courant de votre partie.
Dans un premier temps, vous pouvez faire cela dans une classe dédiée mais à terme, il faurait stocker ces informations dans un fichier.
Vous êtes libre de choisir comment faire mais je vous recommande d'utiliser le format *json*.

Les informations a stocker sont les suivantes :

- le nom du joueur
- le contexte d'action en cours ("combat" ou "mouvement")
- le butin du joueur
- l'équipe du joueur (composée de guerriers, chasseurs et magiciens)

# Liste des actions (méthode) associées à la partie (classe `Game`)  ainsi que leurs explications explication

* config : permet au joueur de configurer sa partie

    - demande le nom du joueur et modifie les données de la partie

##

* start : permet au joueur de recommencer une partie

    - lancer une partie remet la partie à zéro :
        * le nom du joueur est conservé
        * le contexte d'action du joueur et réinitialisé ("mouvement")
        * le butin du joueur est réinitialisé à 40
        * l'équipe du joueur est vide

##

* status : affiche l'état de la partie

    - si le joueur a perdu : affiche gamer over
    - sinon affiche :
        * le nom du joueur
        * la valeur courante du butin 
        * l'équipe du joueur (nombre de guerriers, chasseurs et magiciens)
        * affiche les actions possibles du joueur:
            * si contexte "mouvement" alors possibilité d'acheter ou de se déplacer
            * si contexte "combat" alors possibilité de se battre ou de s'enfuir

##

* buy UNIT : permet au joueur d'acheter une unité 

    - un achat peut être réalisé uniquement hors combat

##

* move DIRECTION : permet au joueur de se déplacer dans une certaine direction
    
    - un déplacement peut être réalisé uniquement hors combat
    - un déplacement débouche sur l'une des situations suivantes :
        * découverte d'un butin avec une probabilité de min(0.2, (chance de l'équipe du joeur / 5) / 100)
        * découverte de soldats errants avec une probabilité de min(0.1, (chance de l'équipe du joeur / 10) / 100)
        * découverte d'une équipe ennemi avec une probabilité de min(0.2, (chance de l'équipe du joeur / 4) / 100)
        * découverte d'un lieu sûr avec une probabilité de 1 - la somme des probabilités des autres événements

##

* fight : permet au joueur de se battre contre l'équipe adverse

    - se battre n'est possible qu'en cas de contexte "combat"
    - le combat est remporté si le score de dégat du joueur est supérieur à celui de l'équipe adverse
    - si le combat est gagné, aucune perte n'est à déplorer, sinon c'est "game over"

##

* flee : permet au joueur de s'enfuir

    - s'enfuir n'est possible qu'en cas de contexte "combat"
    - lors d'une fuite, chaque unité peut mourir:
        * chance de mourir d'une unité : 1 / score de fuite


