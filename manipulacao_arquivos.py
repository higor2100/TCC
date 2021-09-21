#Primeiro arquivo
file = open("arquivo1.html")
fileRead = file.read().replace("","")
file.close()

nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]

file = open(nomeArquivo.replace(":"," -")+".csv","w+")
file.write("Data;Hora;NDeSerie;QtdBites\n"+(tabelaPreConversao.replace("<br>","\n")).replace(" ", ";"))
file.close

#Segundo arquivo 
file = open("arquivo2.html")
fileRead = file.read().replace("","")
file.close()

nomeArquivo = fileRead[fileRead.find("<span>")+len("<span>"):fileRead.find("</span>")]
tabelaPreConversao = fileRead[fileRead.find("<pre>")+len("<pre>"):fileRead.find("</pre>")]

file = open(nomeArquivo.replace(":"," -")+".csv","w+")
file.write("Data;Hora;NDeSerie;QtdBites\n"+(tabelaPreConversao.replace("<br>","\n")).replace(" ", ";"))
file.close