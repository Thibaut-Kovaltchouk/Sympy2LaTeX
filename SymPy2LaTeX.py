#!./envs/bin/python
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

## Bibliothèque à installer avant : pyperclip, PyQt et sympy
import pyperclip as clipboard
from sympy.parsing.sympy_parser import parse_expr
from sympy import latex
import sys
import os
import tempfile
import subprocess
from platform import system
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

## fonctions utiles pour la suite : peuvent être utilisées à part de ce projet !
def latex2showPng(eqlatex):
    """
        Passe du latex vers un png qui s'ouvre
    """
    def os_open(filePath):
        """
            Demande au système d'exploitation d'ouvrir le fichier
            d'adresse filePath
        """
        osType = system()
        if osType == 'Linux':
            # a priori la commande la plus générique pour tous les Linux
            subprocess.call(["xdg-open", filePath])
        elif osType == 'Darwin':
            # pour les mac
            subprocess.call(["open", filePath])
        else : # osType == 'Windows':
            # pas réussi à passer par un subprocess... mais ça marche !
            os.startfile(filePath)
    # on se place dans un dossier temporaire
    tempdir = tempfile.mkdtemp()
    # on crée un document latex de style minimal 
    f = open(tempdir+"/generique.tex","w")
    corps = "\\documentclass[12pt]{minimal}\n" \
            "\\usepackage{amsmath,amsfonts}" \
            "\\begin{document}\n"\
            "$$"+eqlatex+"$$"\
            "\\end{document}"
    # print(corps) Illustration TD PSI* ;)
    # print(list(corps))
    f.write(corps)
    f.close()
    # on utilise latex pour le passer en dvi 
    subprocess.check_call([ "latex", 
                            "-interaction=nonstopmode", 
                            "generique.tex"],
                            cwd=tempdir)
    subprocess.check_call([ "dvipng",
                        "-T","tight",
                        "-D 600",
                        "generique.dvi"], 
                        cwd=tempdir)
    # et on ouvre finalement ce png
    os_open(tempdir+'/generique1.png')

def text2latex(text):
    """
        Passe d'un texte en langage SymPy à du latex
    """
    # on règle le problème des égalités en divisant l'expression
    # en un terme LHS et un RHS
    Lexpr = text.split("=")
    out = ''
    for i, side in enumerate(Lexpr):
        if i > 0: # pour RHS
            out += " = "
        try :
            out += latex(parse_expr(side.strip(),evaluate=False))
        except:
            print("Analyse/Lecture de :", side.strip())
            print("Erreur dans la lecture :", sys.exc_info()[0])
    return out

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
        
        loadUi("interfaceQt/SymPy2LaTeX.ui",self)
        
        # Attribut correspondant au texte copié dans le presse-papier 
        self.OutputTxt = ""

        # Boutons génération png
        # connexion à la méthode pngGenerateAndShow
        self.generate.clicked.connect(self.pngGenerateAndShow)
        
        # Boutons copie dans le presse-papier
        # connexion à la méthode copyLatex2Clipboard
        self.copy.clicked.connect(self.copyLatex2Clipboard)
          
    def texGenerate(self):
        """
            On crée un texte au format latex à partir 
            du texte fourni par l'utilisateur dans 
            la boite de dialogue "inputUser".
        """
        input = self.inputUser.toPlainText()
        self.OutputTxt = text2latex(input)

    def pngGenerateAndShow(self):
        """
            On utilise les fonctionnalités de 
            Sympy pour générer un png ouvrable par 
            n'importe quel logiciel d'affichage d'image 
            (précisé par l'utilisateur dans la boite de 
            dialogue "viewer").
        """
        self.texGenerate()
        try :
            latex2showPng(self.OutputTxt)
        except:
            # gestion de l'erreur très (trop ?) minimaliste
            print("Erreur génération/ouverture png : ", sys.exc_info()[0])
            print("Equation concernée :", self.OutputTxt)

    def copyLatex2Clipboard(self):
        """
            On rajoute la mise en forme nécessaire pour 
            faire fonctionner les bots Discord
        """
        self.texGenerate() # on (re)génère le latex juste avant
        self.OutputTxt
        if self.TeX_Displayed.isChecked():
            out = "\\[\n\\displaystyle" + self.OutputTxt + "\n\\]"
        elif self.TeX_Inline.isChecked():
            out = "$" + self.OutputTxt + "$"
        elif self.TeX_MathBot.isChecked():
            out = "= tex \\displaystyle " + self.OutputTxt
        else :
            out = "$$ \\displaystyle " + self.OutputTxt + "$$"
        # copie dans le presse-papier
        clipboard.copy(out)
        clipboard.paste()

## Lancement de la fenêtre
app = QApplication([])
window = Widget()
window.show()
app.exec_()
