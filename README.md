# 🚄 TGV TRAINY - Explorateur de Graphes Neo4j

TGV Trainy est une application web Flask de recherche d'itinéraires ferroviaires TGV directs ou avec escales, utilisant une base de données orientée graphes Neo4j.

Ce projet a été réalisé dans le cadre du cours Hands-On-BDD orientée graphes - Neo4j à l'ESME.

## Est présent dans ce repository
- Le graphe du projet
- Le code du site flask
- Le code préparation des données
- Le rapport sur l'utilisation de l'ia et explication du site

## 🚀 Installation et Lancement

### 1. Prérequis
Assurez-vous d'avoir Python installé sur votre machine.

### 2. Installation des dépendances
Ouvrez un terminal dans le dossier du projet et tapez : pip install -r requirements.txt

### 3. Préparer la base de donnée
Vérifiez que vous avez bien tgvmax.csv puis lancez Nettoyage.py qui va créer deux fichiers l'un noeud et l'autre relation.
Lancez ensuite importation_neo4j pour implémenter la base dans Neo4j, pour ça changez les valeurs URI et AUTH par les votres.

### 4. Lancer l'application
Vous pouvez désormais lancer app.py puis cliquer sur le lien qui vous est donné ou le lancer sur votre navigateur directement: http://127.0.0.1:5000

Pour le reste je vous invite a regarder notre rapport. 
### Merci !
