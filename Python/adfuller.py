from statsmodels.tsa.stattools import adfuller
import pandas as pd
import datetime

class StationarityTests:
    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def ADF_Stationarity_Test(self, timeseries, printResults = True):
        #Dickey-Fuller test:
        adfTest = adfuller(timeseries, autolag='AIC')
        
        self.pValue = adfTest[1]
        
        if (self.pValue<self.SignificanceLevel):
            self.isStationary = "Sim"
        else:
            self.isStationary = "Não"
        
        if printResults:
            dfResults = pd.Series(adfTest[0:4], index=['Teste de Dickey-Fuller','Valor de P','# Lags Used','# Observations Used'])
            #Add Critical Values
            for key,value in adfTest[4].items():
                dfResults['Valor crítico (%s)'%key] = value
            print('Resultados do Teste de Dickey-Fuller:')
            print(dfResults)


def conversor(strdate):
    objdate = datetime.datetime.strptime(strdate,'%Y-%m-%d %H:%M:%S')
    return objdate

#criação da serie
serie = pd.read_csv("C:\\Users\\Josue\\tcc-final\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")

# 'time' column converted to object datetime
serie['time'] = serie['time'].map(lambda value: conversor(value))
# 'time' is defined as a index
serie = serie.set_index('time')

sTest = StationarityTests()
sTest.ADF_Stationarity_Test(serie, printResults = True)
print("É uma série estacionária?", sTest.isStationary)