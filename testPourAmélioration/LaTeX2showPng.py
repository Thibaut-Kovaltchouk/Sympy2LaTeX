import os
import tempfile
import subprocess
from platform import system

def os_open(filePath):
    osType = system()
    if osType == 'Linux':
        subprocess.call(["xdg-open", filePath])
    elif osType == 'Darwin':
        subprocess.call(["open", filePath])
    else : # osType == 'Windows':
        os.startfile(filePath)

eqlatex="x=a"
tempdir = tempfile.mkdtemp()
f= open(tempdir+"/generique.tex","w")
corps = "\\documentclass[12pt]{minimal}\n" \
                "\\usepackage{amsmath,amsfonts}" \
                "\\begin{document}" \
                "\\fontsize{60}{72}\n"\
                "$$"+eqlatex+"$$"\
                "\\end{document}"
f.write(corps)
f.close()
subprocess.check_call(['latex' , '-interaction=nonstopmode' , 'generique.tex'] ,cwd=tempdir)
subprocess.check_call(['dvipng' , 'generique.dvi'], cwd=tempdir)
os_open(tempdir+'/generique1.png')
# remove tex dvi png log ...