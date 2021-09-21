import pandas as pd

tabelaUpload = pd.read_csv("PACS01 - Trafego Out VDX PACS01_To_CORE02.csv", sep=";")[::-1]
tabelaDownload = pd.read_csv("PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=";")[::-1]
print(tabelaUpload)
print("**********************************************************************")
print(tabelaDownload)
