# Sympy2LaTeX

## Présentation
Un projet pour aider les étudiants qui ont des difficultés avec l'utilisation de LaTeX sur les serveurs Discord.

## TLDR ;) (Pas le temps de tout lire)

* install.sh/bat suivant votre os puis rendre Sympy2Latex.py exécutable. 
* conda doit être dans le PATH (local ou système) pour l'installation, sinon, créer l'environnement manuellement avec la commande `conda create --prefix ./envs --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y`
* LaTeX (et une visioneuse d'image png) nécessaire pour la visualisation

## Installation

Pour l'instant : conda est nécessaire pour le bon fonctionnement du projet, ainsi que LaTeX pour la prévisualisation. Je vous conseille de simplement télécharger ou vous cloner l'ensemble du dépôt

### Choix 1 (déconseillé) 
Vous utilisez votre environnement conda préféré pour faire fonctionner le script SymPy2LaTeX.py. Par exemple, sous Pyzo avec le raccourci ctrl+shift+E. 

Pour installer les dépendances Python : 

```bash
conda install --channel conda-forge sympy=1.5 PyQt pyperclip=1.7 -y
```

Choix déconseillé car votre installation de Conda et Python n'est pas forcément au même niveau que celle de ce projet, ce qui peut entraîner des conflits de versions.

### Choix 2 (conseillé)

Une fois le téléchargement fini, vous installer le dossier là où vous voulez le voir apparaître puis vous lancez `bash install.sh` (pour mac et linux) ou vous executez install.bat (pour windows) pour créer l'environnement conda local.

Pour l'utilisation, tout ce qu'il vous reste à faire, c'est de lancer le fichier en double-cliquant dessus après l'avoir rendu exécutable SymPy2LaTeX.py. Des lanceurs de secours sont présents : SymPy2LaTeX.sh pour mac et linux et SymPy2LaTeX.bat pour windows.

Pour créer des raccourcis (ça peut être pratique), vous avez accès à des icônes.

**Si vous ne savez pas comment lancez un fichier \*.sh ou \*.bat sur votre système d'exploitation, des liens sont donnés dans la suite du texte**

### Dans tous les cas :

#### Installation de conda si nécessaire

Je vous conseille miniconda, plus léger (python 3.7, 64 bits a priori) :
 
https://docs.conda.io/en/latest/miniconda.html

**Attention, pour le bon fonctionnement des scripts bash (\*.sh ou \*.bat) fournis, il faut que le chemin vers conda soit ajouter au variable d'environnement, ce qui n'est pas le cas dans l'installation par défaut sous Windows. Je vous invite à ajouter au *PATH* global ou local le chemin vers conda (apriori, quelque-chose qui ressemble à C:\Users\jsmith\Anaconda3) **

Un guide pour modifier les variables d'environnement dans un cas similaire : https://thepingouin.com/2020/01/04/windows-10-ajouter-python-aux-variables-denvironnement/

#### Installation de LaTeX si nécessaire

Les utilisateurs ont besoins d'une installation de LaTeX pour la visualisation (+ dvipng si la distribution de LaTeX que l'utilisateur possède ne le contient pas déjà, en particulier avec TeX Live).

Conseil pour les distribution LaTeX : MacTeX pour Mac, TeX Live pour Linux et MiKTeX pour Windows :
* Pour MaxTeX : https://www.tug.org/mactex/mactex-download.html
* Pour MiKTeX : https://miktex.org/download
* Pour Linux : utilisez votre gestionnaire de paquet préféré.

#### Guide pour rendre des fichiers exécutables

* Pour mac et linux : chmod +x nomDuFichier.extension https://support.apple.com/fr-fr/guide/terminal/apdd100908f-06b3-4e63-8a87-32e71241bab4/mac
* Pour Windows : double-cliquer et si ça ne marche pas ... TOCOMPLETE ...

## Astuce 

Une fois que vous avez trouvé un logiciel visionneur d'image qui vous convient, changez la ligne 17 du script Sympy2Latex.py pour l'avoir toujours par défaut.

## Tests 

Pour l'instant, les tests ont montrés : (je suis seul à avoir testé pour l'instant)

- [x] Lubuntu 20.04 : TeX Live + dvipng + miniconda
- [x] Windows 10 : MiKTeX + miniconda

## Bug connu

* Je n'arrive pas à créer un lanceur efficace sous Linux : la fenêtre se ferme tout de suite.

## Résolution d'un bug basique

Si cela a marché mais que cela ne marche plus, essayer de supprimer le dossier envs et de relancer install.sh/bat (suivant votre système d'expoitation). Sinon, clonez de nouveau ce dépôt.

Premier projet sur GitHub !
