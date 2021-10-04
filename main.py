import os

exec(compile(open('manipulacao_arquivos.py', "rb").read(), 'manipulacao_arquivos.py', 'exec'), globals(), locals())
path = "./Jupyter/Arquivo CSV/"
files = os.listdir(path)
def jupyterFile(f):    
    abrir = open("modelo")
    if f.find("In")!=-1:
        abrirLeitura = abrir.read().replace("download","upload").replace("REPORLOCAL","./Arquivo CSV/"+f)
    else:
        abrirLeitura = abrir.read().replace("REPORLOCAL","./Arquivo CSV/"+f)
    abrir.close()

    salvar = open("./Jupyter/"+f[0:f.find(".csv")]+".ipynb","w")
    salvar.write(abrirLeitura)
    salvar.close()

for f in files:
    jupyterFile(f)

