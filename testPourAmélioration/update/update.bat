@ECHO OFF
::  on se déplace vers le dossier de travail
echo "%0"
echo "%~dp0"
cd "%~dp0""
::  conda doit etre installe avant et etre accessible
conda update conda
echo conda a jour pour la creation du nouvel environnememt
::  ajout des librairies nécessaires 
conda install --channel conda-forge sympy=1.5 PyQt pyperclip=1.7 -y
echo environnement conda cree
echo fin des installations
