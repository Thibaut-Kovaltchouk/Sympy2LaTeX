#!/bin/bash
# on se déplace vers le dossier de travail
echo "$0"
echo "$(dirname "${0}")"
cd "$(dirname "${0}")"
# conda doit être installé avant et être accessible
eval "$(conda shell.bash hook)"
conda activate ./envs
echo environnement conda activé
# On lance
python SymPy2LaTeX.py
echo fermeture de la fenêtre
