# Sympy2LaTeX

## Présentation
Un projet pour aider les étudiants qui ont des difficultés avec l'utilisation de LaTeX sur les serveurs Discord.

## Installation

Pour l'instant : conda est nécessaire pour le bon fonctionnement du projet, ainsi que LaTeX pour la prévisualisation.

### Choix 1 (déconseillé) 
Vous téléchargez uniquement Minimal.zip (4 ko) et vous utilisez votre environnement conda préféré pour faire fonctionner le script SymPy2LaTeX.py. Par exemple, sous Pyzo avec le raccourci ctrl+shift+E. 

Pour installer les dépendances Python : 

```bash
conda install --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y
```

### Choix 2 (conseillé)

**Si vous ne savez pas comment lancez un fichier \*.sh sur votre système d'exploitation, des liens sont donnés dans la suite du texte**

Vous utilisez uniquement Minimal.zip (4 ko). Une fois le téléchargement fini, vous installer le dossier là où vous voulez le voir apparaître puis vous lancez install.sh pour créer l'environnement conda local (juste besoin d'un droit d'écriture du dossier normalement).

Pour l'utilisation, tout ce qu'il vous reste à faire, c'est de lancer le fichier SymPy2LaTeX.sh.

### Choix 3 (bazooka pour écraser une mouche)

Vous téléchargez tout le projet et vous pouvez donc utiliser l'environnement conda du projet. C'est plus lourd forcément... et vous remplacer le temps d'installation de l'environnement conda par un temps de téléchargement. A vous de voir.

### Dans tous les cas :

#### Installation de conda si nécessaire

Je vous conseille miniconda, plus léger (python 3.7, 64 bits a priori) :
 
https://docs.conda.io/en/latest/miniconda.html

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
- [ ] Windows 10 : MiKTeX + miniconda (je redémarre tout de suite et je vous le dis)

Premier projet sur GitHub !
