#!/bin/bash
# on se déplace vers le dossier de travail
echo "$0"
echo "$(dirname "${0}")"
cd "$(dirname "${0}")"
# conda doit être installé avant et être accessible
eval "$(conda shell.bash hook)"
conda create --prefix ./envs --channel conda-forge python=3.7 sympy=1.5 PyQt pyperclip=1.7 -y
echo environnement conda créé
echo fin des installations
