# 4A_SQR_an_war
Nous sommes Waren Muguel Mba Wega, Anïck Ryane Mouafo Mawetze et El Hafidy Salma étudiants en 4A SQR et nous dévéloppons en Python.
#
Sujet guidé : Un chemin tout tracé. Nous avons choisi ce sujet car nous sommes encore dans nos débuts et nous estimons que le TP guidé contrairement à l'autre va nous permettre de comprendre en détail et mener comme il se doit notre projet.
#
### 2.1.2 Procédure de chargement de données dans l’API à partir d’un fichier .cvs
* Le bout de code destiné à effectuer cette tâche ouvrira le fichier CSV 'fichier.csv' et lira chaque ligne en utilisant 'csv.reader()'. La méthode next() permettra de sauter la première ligne du fichier afin de distinguer les entêtes aux données. Nous fournissons ensuite un format: 'sender,receiver,Amount,date' , qui permettra de remplir les lignes de notre tableau de transactions 'list_of_transactions'. Aussi nous convertissons la valeur du montant de la transaction à l'aide la commande 'float(Amount)'.

* Le lien vers le Swagger Editor fournit dans l'énoncé du projet nous a permis de designer notre API. Ainsi, une documentation interactive sur notre API sera visible depuis le fichier swagger.yaml.



 https://github.com/Anick123/4A_SQR_an_war/edit/main/README.md
 ![alt text](https://img-ik.cars.co.za/news-site-za/images/2022/06/a45-dyn.jpg?tr=h-347%2Cw-617)
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
Déploiement d'une première release publique de l’API 
[![Docker push GCR](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml/badge.svg)](https://github.com/Anick123/4A_SQR_an_war/actions/workflows/Build_to_GCR.yml)

