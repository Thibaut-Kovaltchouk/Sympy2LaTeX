#!/usr/bin/bash
# on se déplace vers le dossier de travail
echo "$0"
echo "$(dirname "${0}")"
cd "$(dirname "${0}")"
# conda doit être installé avant et être accessible
eval "$(conda shell.bash hook)"
# un environnement doit être déjà présent avec python 3.7
conda activate ./envs
echo environnement conda activé
conda install --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y
echo installation terminé
