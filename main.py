import os
dir_path = os.path.dirname(os.path.realpath(__file__))
exec(compile(open(dir_path+"\manipulacao_arquivos.py", "rb").read(), dir_path+"\manipulacao_arquivos.py", 'exec'), globals(), locals())
path = dir_path+"\Jupyter\Arquivo CSV\\"
files = os.listdir(path)
def jupyterFile(f):    
    abrir = open(dir_path+"\modelo")
    abrirLeitura = abrir.read().replace("arquivoTxt",f[0:f.find(".csv")]).replace("arquivoNpy",f[0:f.find(".csv")]).replace("arquivoPkl",f[0:f.find(".csv")]).replace("download","bytes").replace("Download","bytes").replace("REPORLOCAL","./Arquivo CSV/"+f)
    abrir.close()

    salvar = open(dir_path+"\Jupyter\\"+f[0:f.find(".csv")]+".ipynb","w")
    salvar.write(abrirLeitura)
    salvar.close()

for f in files:
    jupyterFile(f)

