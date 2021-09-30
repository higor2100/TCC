import pandas as pd
import os

path = "./Arquivo HTML/"
files = os.listdir(path)

def manipular(file):
    #1 - Abertura do arquivo em HTML
    abrir = open(path+f)
    abrirLeitura = abrir.read().replace("","")
    abrir.close()

    #2 - Manipulação do arquivo em HTML
    nomeArquivo = abrirLeitura[abrirLeitura.find("<span>")+len("<span>"):abrirLeitura.find("</span>")]
    tabelaPreConversao = abrirLeitura[abrirLeitura.find("<pre>")+len("<pre>"):abrirLeitura.find("</pre>")]
    conv = (tabelaPreConversao.replace("<br>","\n")).replace(" ", ";")

    #3 - Criação da Base de dados
    if nomeArquivo.find("In"):
        tabelaUpload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','upload'])
    else:
        tabelaUpload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','download'])
    tabelaUpload.insert(0,"time",tabelaUpload['Data'] + " " + tabelaUpload['Hora'])

    #4 - Limpeza dos dados desnecessarios
    del tabelaUpload['NDeSerie'],tabelaUpload['Data'],tabelaUpload['Hora']
    tabelaUpload = tabelaUpload[:-1]

    #5 - Formatação dos dados 
    tabelaUpload['time'] = pd.to_datetime(tabelaUpload['time'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
    if nomeArquivo.find("In"):
        tabelaUpload['upload'] = tabelaUpload['upload'].astype(object).astype(int)
    else:
        tabelaUpload['download'] = tabelaUpload['download'].astype(object).astype(int)
    
    #6 - Salvamento do arquivo em formato CSV
    tabelaUpload[::-1].to_csv(r"./Jupyter/Arquivo CSV/"+nomeArquivo.replace(":"," -")+".csv",index = False, header=True)

for f in files:
    manipular(f)