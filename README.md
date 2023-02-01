# 4A_SQR_an_war
Nous sommes Waren Muguel Mba Wega, Anïck Ryane Mouafo Mawetze et El Hafidy Salma étudiants en 4A SQR à l'ESIREM et nous dévéloppons en Python.

![alt text](https://esirem.u-bourgogne.fr/wp-content/uploads/2021/02/cropped-sans-titr-petite2-1.png)

Notre README peut etre accessible via: https://github.com/Anick123/4A_SQR_an_war/edit/main/README.md
#
### Sujet guidé : Un chemin tout tracé. 
Nous avons choisi ce sujet car nous sommes encore dans nos débuts et nous estimons que le TP guidé contrairement à l'autre va nous permettre de comprendre en détail et mener comme il se doit notre projet.
#
### 2.1.2 Procédure de chargement de données dans l’API à partir d’un fichier .cvs
* Le bout de code destiné à effectuer cette tâche ouvrira le fichier CSV 'fichier.csv' et lira chaque ligne en utilisant 'csv.reader()'. La méthode next() permettra de sauter la première ligne du fichier afin de distinguer les entêtes aux données. Nous fournissons ensuite un format: 'sender,receiver,Amount,date' , qui permettra de remplir les lignes de notre tableau de transactions 'list_of_transactions'. Aussi nous convertissons la valeur du montant de la transaction à l'aide la commande 'float(Amount)'.

* Le lien vers le Swagger Editor fournit dans l'énoncé du projet nous a permis de designer notre API. Ainsi, une documentation interactive sur notre API sera visible depuis le fichier swagger.yaml accessible depuis https://editor.swagger.io/.
 
 
 # Statuts actions
![alt](http://github.com/Anick123/4A_SQR_an_war/actions/workflows/blank.yml/badge.svg)
![alt](http://github.com/Anick123/4A_SQR_an_war/actions/workflows/curl.yml/badge.svg)
![alt](http://github.com/Anick123/4A_SQR_an_war/actions/workflows/action.yml/badge.svg)


## 2.1.3 Préparer l’intégration continue (CI)
Ici on retrouve les badges pour les différents githubs actions crées, notamment : 
*  Une déclenchée à chaque changement pour builder l’application. 
![alt](http://github.com/Anick123/4A_SQR_an_war/actions/workflows/builder.yml/badge.svg)
* Une déclenchée manuellement pour utiliser le fichier Dockerfile pour créer une image.
![alt](http://github.com/Anick123/4A_SQR_an_war/actions/workflows/build_Dockerfile.yml/badge.svg)

## 2.1.5 Top départ
Déploiement d'une première release publique de l’API. La version à ce niveau est: v1.0.0 car cette version sera encore améliorée plus tard.
[![Docker push GCR](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml/badge.svg)](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml)

## 2.1.6 Amélioration de l’API
Dans cette partie, pour chacune des fonctionnalités ajoutées, nous faisons une release de notre API avec le numéro de
version adapté.
* Nous avons choisi comme version de notre 2ème release la version v1.1.0 car nous considerons que c'est une amélioration considérable. Parmi toutes les fonctions de hashage, nous avons choisi la fonction de hachage cryptographique hashlib.sha256 car celle-ci est la plus avantageuse de par :

##### Sécurité : elle permet de garantir l'intégrité des données en générant un hachage unique pour chaque entrée.

##### Fiabilité : elle est une fonction de hachage fiable et bien établie qui a été largement utilisée dans de nombreuses applications critiques.

##### Vitesse : elle peut générer rapidement un hachage pour de grandes quantités de données.

##### Simplicité : elle est simple et facile à utiliser, ce qui en fait un choix populaire pour les développeurs.

##### Prise en charge multilingue : elle est disponible dans de nombreux langages de programmation, ce qui en fait un choix pratique pour les développeurs travaillant sur des projets multilingues.

L'ajout du hash d’une transaction dans son modèle: (P1, P2, t, s, h) peut etre vérifié par le badge suivant : [![Docker push GCR](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml/badge.svg)](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml)

* Vérification de l’intégrité des données envoyées en recalculant les hashs à partir des données envoyées et en les comparant avec les hashs stockés
précédemment [![Docker push GCR](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml/badge.svg)](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml)
* Correction du calcul de hash en prenant en compte le paramètre t : la date de transfert.
[![Docker push GCR](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml/badge.svg)](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml)
