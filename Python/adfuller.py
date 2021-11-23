from statsmodels.tsa.stattools import adfuller
import pandas as pd
import datetime

class Estacionariedade:
    def __init__(self, t=.05):
        self.testeTAU = t
        self.pValue = None
        self.estacionaria = None

    def TesteDF(self, seriestemporais, printResults = True):
        #Teste de Dickey-Fuller:
        testeDF = adfuller(seriestemporais, autolag='AIC')
        
        self.pValue = testeDF[1]
        
        if (self.pValue<self.testeTAU): #rejeita H0
            self.estacionaria = "Sim"
        else: #aceita H0
            self.estacionaria = "Não"
        
        if printResults:
            #print("teste", testeDF)
            dfResultados = pd.Series(testeDF[0:4], index=['Teste de Dickey-Fuller','Valor de P','Atrasos','Amostra'])
            #Add Critical Values
            for key,value in testeDF[4].items():
                dfResultados['Valor crítico (%s)'%key] = value
            print('Resultados do Teste de Dickey-Fuller:')
            print(dfResultados)


def conversor(strdate):
    objdate = datetime.datetime.strptime(strdate,'%Y-%m-%d %H:%M:%S')
    return objdate

#criação da serie
serie = pd.read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")

# 'time' conversão para datetime
serie['time'] = serie['time'].map(lambda value: conversor(value))
# 'time' vira um index
serie = serie.set_index('time')

Teste = Estacionariedade()
Teste.TesteDF(serie, printResults = True)
print("É uma série estacionária?", Teste.estacionaria)