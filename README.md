# **OCR-Python-2**

# **Projet 2 :** Utilisez les bases de Python pour l'analyse de marché

Vous êtes analyste marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion. Dans le cadre de vos fonctions, vous essayez de suivre manuellement les prix des livres d'occasion sur les sites web de vos concurrents, mais cela représente trop de travail et vous n'arrivez pas à y faire face : il y a trop de livres et trop de librairies en ligne ! Vous et votre équipe avez décidé d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne.

**Site : http://books.toscrape.com/**

## Utilisation

### Environnement virtuel

Pour mettre en place l'environnement virtuel nécessaire pour faire fonctionner le script, procéder comme suit :

Dans un terminal ouvert dans le dossier où vous avez cloné le repository, créez un environnement virtuel a l'aide de venv :

> python3 -m venv [nom environnement]

Une fois que l'environnement est créé, activez l'environnement (dans cet exemple, 'env' est le nom de mon environnement) :

> **Windows** : .\env\Scripts\activate

> **Mac / Linux** : source env/bin/activate

Si l'environnement c'est bien activé, le nom de l'environnement s'affichera à gauche de l'indicateur de position dans le terminal

Installez tout les packages listé dans le fichier 'requirements.txt' dans votre environnement virtuel :

> pip install -r requirements.txt

Vérifier que tout les packages sont bien installé a l'aide de la commande pip freeze.

### Lancement du Parse 

> python main.py
