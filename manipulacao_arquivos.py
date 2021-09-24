import pandas as pd

#Primeiro arquivo
#1 - Abertura do arquivo em HTML
file = open("arquivo1.html")
fileRead = file.read().replace("","")
file.close()

#2 - Manipulação do arquivo em HTML
nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]
conv = (tabelaPreConversao.replace("<br>","\n")).replace(" ", ";")

#3 - Criação da Base de dados
tabelaUpload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','download'])
tabelaUpload.insert(0,"time",tabelaUpload['Data'] + " " + tabelaUpload['Hora'])

#4 - Formatação dos dados 
tabelaUpload['time'] = pd.to_datetime(tabelaUpload['time'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
tabelaUpload['download'] = pd.to_numeric(tabelaUpload['download'])

#5 - Limpeza dos dados desnecessarios
del tabelaUpload['NDeSerie'],tabelaUpload['Data'],tabelaUpload['Hora']
tabelaUpload = tabelaUpload[:-1]

#6 - Salvamento do arquivo em formato CSV
tabelaUpload[::-1].to_csv(r"./"+nomeArquivo.replace(":"," -")+".csv",index = False, header=True)

##################################################################################################################################

#Segundo arquivo 
#Repete o mesmo passo acima
file = open("arquivo2.html")
fileRead = file.read().replace("","")
file.close()

nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]
conv = (tabelaPreConversao.replace("<br>","\n")).replace(" ", ";")

tabelaDownload = pd.DataFrame([x.split(';') for x in conv.split('\n')],columns=['Data','Hora','NDeSerie','download'])
tabelaDownload.insert(0,"time",tabelaDownload['Data'] + " " + tabelaDownload['Hora'])

tabelaDownload['time'] = pd.to_datetime(tabelaDownload['time'], format='%d-%m-%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
tabelaDownload['download'] = pd.to_numeric(tabelaDownload['download'])

del tabelaDownload['NDeSerie'],tabelaDownload['Data'],tabelaDownload['Hora']
tabelaDownload = tabelaDownload[:-1]

tabelaDownload[::-1].to_csv(r"./"+nomeArquivo.replace(":"," -")+".csv",index = False, header=True)

##################################################################################################################################
#Salvamento em XLSX para analise de Dados com Excel
with pd.ExcelWriter('UnirEmExcel.xlsx') as writer:
    tabelaUpload.to_excel(writer,sheet_name="Upload",index=False)
    tabelaDownload.to_excel(writer,sheet_name="Download",index=False)