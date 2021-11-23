import os
from datetime import datetime, date
dir_path = os.path.dirname(os.path.realpath(__file__))
exec(compile(open(dir_path+"\manipulacao_arquivos.py", "rb").read(), dir_path+"\manipulacao_arquivos.py", 'exec'), globals(), locals())
path = dir_path+"\Jupyter\Arquivo CSV\\"
files = os.listdir(path)
def jupyterFile(f):    
    abrir = open(dir_path+"\modelo")
    abrirLeitura = abrir.read().replace("arquivoTxt",f[0:f.find(".csv")]).replace("arquivoNpy",f[0:f.find(".csv")]).replace("arquivoPkl",f[0:f.find(".csv")]).replace("download","bits").replace("Download","bits").replace("REPORLOCAL","./Arquivo CSV/"+f).replace("#GERADOR",  datetime.today().strftime("%d.%m.%Y"))
    abrir.close()
    if f.find("In") != -1:
        salvar = open(dir_path+"\Jupyter\\In - "+datetime.today().strftime("%d.%m.%Y_%H.%M.%S") +".ipynb","w")
    else:
        salvar = open(dir_path+"\Jupyter\\Out - "+datetime.today().strftime("%d.%m.%Y_%H.%M.%S") +".ipynb","w")
    salvar.write(abrirLeitura)
    salvar.close()

for f in files:
    jupyterFile(f)