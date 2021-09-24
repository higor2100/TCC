from numpy.core.fromnumeric import partition
import pandas as pd
#Primeiro arquivo
file = open("arquivo1.html")
fileRead = file.read().replace("","")
file.close()

nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]
conv = (tabelaPreConversao.replace("<br>","\n")).replace(" ", ";")

tabelaUpload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','QtdBites'])
tabelaUpload.insert(0,"Data Hora",tabelaUpload['Data'] + " " + tabelaUpload['Hora'])

tabelaUpload['Data Hora'] = pd.to_datetime(tabelaUpload['Data Hora'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
del tabelaUpload['NDeSerie'],tabelaUpload['Data'],tabelaUpload['Hora']
tabelaUpload = tabelaUpload[:-1]

tabelaUpload[::-1].to_csv(r"./"+nomeArquivo.replace(":"," -")+".csv",index = False, header=True)


#Segundo arquivo 
file = open("arquivo2.html")
fileRead = file.read().replace("","")
file.close()

nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]
conv = (tabelaPreConversao.replace("<br>","\n")).replace(" ", ";")

tabelaDownload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','QtdBites'])
tabelaDownload.insert(0,"Data Hora",tabelaDownload['Data'] + " " + tabelaDownload['Hora'])

tabelaDownload['Data Hora'] = pd.to_datetime(tabelaDownload['Data Hora'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
del tabelaDownload['NDeSerie'],tabelaDownload['Data'],tabelaDownload['Hora']
tabelaDownload = tabelaDownload[:-1]

tabelaDownload[::-1].to_csv(r"./"+nomeArquivo.replace(":"," -")+".csv",index = False, header=True)
