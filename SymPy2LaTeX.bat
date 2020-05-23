@ECHO OFF
::  on se déplace vers le dossier de travail
echo "%0"
echo "%~dp0"
cd "%~dp0""
::  conda doit etre installe avant et etre accessible
call conda activate ./envs
echo environnement conda active
:: On lance le script
python SymPy2LaTeX.py
echo fermeture de la fenetre
call conda deactivate
echo sortie de l'environnement
pause
