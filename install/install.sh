#!/usr/bin/env sh
# on se déplace vers le dossier de travail
echo "$0"
echo "$(dirname "${0}")"
cd "$(dirname "${0}")"
cd ..
echo $PWD
# conda doit être installé avant et être accessible
eval "$(conda shell.bash hook)"
conda update conda -y
echo conda à jour pour la création du nouvel environnememt
conda create --prefix ./envs --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y
echo environnement conda créé
echo fin des installations
