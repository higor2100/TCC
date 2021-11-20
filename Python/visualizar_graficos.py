import pandas as pd
from matplotlib import pyplot
f = open("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Python\\info.txt")
txt = f.read()
f.close()
df = pd.read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")
"""
dados = txt[txt.find("[")+1:txt.find("]")].replace(",", "")

tabela = pd.DataFrame(dados.split(" "),columns=["Simulação"])
tabela["Dias"] = tabela.index
tabela = tabela.iloc[:, ::-1]
tabela = pd.to_numeric(tabela["Simulação"])

print(tabela)
"""
del df["time"]
df.drop(df.tail(15000).index,inplace=True)
print(df["bytes"])
pyplot.plot(df)
pyplot.show()
