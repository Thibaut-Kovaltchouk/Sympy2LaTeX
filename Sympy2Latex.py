#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Petite interface graphique pour gagner du temps dans l'écriture des 
    équations sur Discord ou autre : le langage Sympy peut être bien plus 
    économe que latex, et un peu moins dur à prendre en main
    Enjoy ;). Si vous avez des retours, n'hésitez pas !
    Et j'encourage quiconque voudrait améliorer cette petite interface
    à le faire. J'ai essayé de documenter au mieux...
    TK
"""

## visionneur par défaut : à changer
# mettre le chemin d'accès complet
# si ça ne marche pas en ne mettant 
# que le nom du logiciel
visio = "mspaint" # a priori, pour Windows
# Attention : dvipng à installer pour Linux
# (avec votre gestionnaire de packet préféré)
# ça devrait pas poser de problème
# visio = "lximage-qt" # a priori, pour Lubuntu
# TODO compléter pour tous les OS possibles

## Bibliothèque à installer
# conda install pyperclip, sympy, PyQt
import pyperclip as clipboard
from sympy import oo, I, Matrix
from sympy.functions import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import latex, preview
import sys
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

## Définition du fonctionnement de la fenêtre

class Widget(QMainWindow):
    """
        Class correspondant à la fenêtre principale
    """
    def __init__(self):
        """
            Initialisation des attributs OutputFormat et 
            OutputTxt et connexions des signaux des 
            différents boutons aux méthodes :
                - pngGenerateAndShow
                - copyLatex2Clipboard
        """

        QMainWindow.__init__(self)
        
        loadUi("interfaceSympy2LaTeX.ui",self)
        
        # Attribut correspondant au format désiré de sortie 
        self.OutputFormat = "MathBot"
        # Attribut correspondant au texte copié dans le presse-papier 
        self.OutputTxt = ""

        # on prend en compte la valeur par défaut précisé par l'utilisateur
        # au début du script
        self.viewer.setText(visio)

        # Boutons génération png
        # connexion à la méthode pngGenerateAndShow
        self.generate.clicked.connect(self.pngGenerateAndShow)
        
        # Boutons génération png
        # connexion à la méthode pngGenerateAndShow
        self.copy.clicked.connect(self.copyLatex2Clipboard)
          
    def texGenerate(self):
        """
            On crée un texte au format latex à partir 
            du texte fourni par l'utilisateur dans 
            la boite de dialogue "inputUser".
        """
        input = self.inputUser.toPlainText()
        # on règle le problème des égalités en divisant l'expression
        # en un terme LHS et un RHS
        Lexpr = input.split("=")
        self.OutputTxt = ''
        for i, side in enumerate(Lexpr):
            if i > 0: # pour RHS
                self.OutputTxt += " = "
            try :
                self.OutputTxt += latex(parse_expr(side.strip(),evaluate=False))
            except:
                print("Unexpected error:", sys.exc_info()[0])

    def pngGenerateAndShow(self):
        """
            On utilise les fonctionnalités de 
            Sympy pour générer un png ouvrable par 
            n'importe quel logiciel d'affichage d'image 
            (précisé par l'utilisateur dans la boite de 
            dialogue "viewer").
        """
        self.texGenerate()
        if self.OutputTxt != "":
            # Début du fichier LaTeX avec réglage de la taille
            # afin de limiter la pixellisation
            debut = "\\documentclass[12pt]{minimal}\n" \
                    "\\usepackage{amsmath,amsfonts}" \
                    "\\begin{document}" \
                    "\\fontsize{60}{72}\n"
            softwareViewer = self.viewer.text()
            preview("$$" + self.OutputTxt + "$$", 
                euler=False,
                output='png',
                preamble = debut,
                viewer=softwareViewer)

    def copyLatex2Clipboard(self):
        """
            On rajoute la mise en forme nécessaire pour 
            faire fonctionner les bots Discord
        """
        self.texGenerate() # on (re)génère le latex juste avant, on sait jamais
        self.OutputTxt
        if self.TeX_Displayed.isChecked():
            out = "\\[\n\\displaystyle" + self.OutputTxt + "\n\\]"
        elif self.TeX_Inline.isChecked():
            out = "$" + self.OutputTxt + "$"
        elif self.TeX_MathBot.isChecked():
            out = "= tex \\displaystyle " + self.OutputTxt
        else :
            out = "$$ \\displaystyle " + self.OutputTxt + "$$"
        # co
        clipboard.copy(out)
        clipboard.paste()

## Lancement de la fenêtre
app = QApplication([])
window = Widget()
window.show()
app.exec_()