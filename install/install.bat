@ECHO OFF
::  on se déplace vers le dossier de travail
echo "%0"
echo "%~dp0"
cd "%~dp0""
cd ..
echo %cd%
::  conda doit etre installe avant et etre accessible
conda update conda -y
echo conda a jour pour la creation du nouvel environnememt
::  creation local de l'environnement local 
conda create --prefix ./envs --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y
echo environnement conda cree
echo fin des installations
