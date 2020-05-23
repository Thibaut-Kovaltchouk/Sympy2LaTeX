# Sympy2LaTeX

## Présentation
Un projet pour aider les étudiants qui ont des difficultés avec l'utilisation de LaTeX sur les serveurs Discord.

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

Une fois le téléchargement fini, vous installer le dossier là où vous voulez le voir apparaître puis vous lancez install.sh pour créer l'environnement conda local (juste besoin d'un droit d'écriture du dossier normalement).

Pour l'utilisation, tout ce qu'il vous reste à faire, c'est de lancer le fichier SymPy2LaTeX.sh (pour mac et linux) ou SymPy2LaTeX.bat (pour windows) avec une commande bash. Pour ajouter des raccourcis, vous avez accès à des icônes.

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

#### Guide pour lancer des fichiers shell suivant votre OS (\*.sh)

* Pour Mac : https://support.apple.com/fr-fr/guide/terminal/apdd100908f-06b3-4e63-8a87-32e71241bab4/mac
* Pour Linux : dans le terminal correspondant à la fenêtre (F4 sur Lubuntu) : bash fichier.sh
* Pour Windows : 
    * Installer et faire fonctionner win-bash : http://win-bash.sourceforge.net/ puis, dans le terminal, bash cheminRelatifCompletFichier\_sh ou bash cheminAbsoluFichier\_sh
    * Ou utiliser le shell bash Linux sous Windows : https://korben.info/installer-shell-bash-linux-windows-10.html
    * dans le terminal, bash cheminRelatifCompletFichier\_sh ou bash cheminAbsoluFichier\_sh (pour récupérer cela efficacement, utilisez la barre de navigation Windows ou sinon, clique droit propriété)

## Astuce 

Une fois que vous avez trouvé un logiciel visionneur d'image qui vous convient, changez la ligne 17 du script Sympy2Latex pour l'avoir toujours par défaut.

## Tests 

Pour l'instant, les tests ont montrés : (je suis seul à avoir testé pour l'instant)

- [x] Lubuntu 20.04 : TeX Live + dvipng + miniconda
- [x] Windows 10 : MiKTeX + miniconda

Premier projet sur GitHub !
