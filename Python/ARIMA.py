#############################################
#  Grid Search ARIMA model hyperparameters  #
#############################################
#
# from Brownlee, Jason - "Introduction to time series forecasting with Python"
#
import warnings
from pandas import read_csv
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import time

warnings.filterwarnings("ignore")
inicio = time.time()

# evaluate an ARIMA model for a given order (p,d,q)


def arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X)*0.999)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    for t in test:
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()
        predictions.append(int(yhat[0][0]))
        history.append(t)
    # calculate out of sample error
    return predictions, test
# load dataset
df = read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")

#leitura e remoção de dados do arquivo csv
tabela = df['bits']

# evaluate parameters
predicao, teste = arima_model(tabela.head(len(tabela)-6), (1,0,0))
pyplot.plot(teste)
previsao = [x for x in predicao]
print(previsao.index(int(39067087.08319867)))
len(predicao)
pyplot.plot(previsao, color='red')
pyplot.show()
fim = time.time()
print(str(round((inicio-fim)/60,0))+' mins')
erro = "Erro de In em " + str(0.999*100)  +"%:\r\nValor Original: \t\tPrevisão: \t\tErro:\r\n"
i = 0
for e in tabela:
    if i>=5:
        break
    erro+= str(e)+"\t\t\t\t"+str(predicao[i])+"\t=\t"+str(abs(round(100*(e/predicao[i]),2))) + "%\r\n"
    i+=1
print(erro)
"""
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from numpy import mean
from math import sqrt
import time

inicio = time.time()

#criação do dataframe
df = read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")

#leitura e remoção de dados do arquivo csv
X = df['bytes']
S = X.tail(5).values.tolist()
X.drop(X.tail(5).index,inplace=True)
valores = X.values.tolist()
porcento = 0.66
tamanho = int(len(X) * porcento)
treinamento, segundoQuartil= [x for x in valores[0:tamanho]], [x for x in valores[tamanho:len(X)]]
predicoes = list()

#criação do modelo
for t in range(len(segundoQuartil)-1,-1,-1):
    modelo = ARIMA(treinamento, order=(1,0,1))
    modelo_fit = modelo.fit()
    saida = int(mean(modelo_fit.forecast(steps=3)))
    predicoes.append(saida)
    treinamento.append(segundoQuartil[t])
# Teste RMSE com as predições
#rmse = sqrt(mean_squared_error(segundoQuartil, predicoes))
#print('Teste do RMSE: %.3f' % rmse)

# plot das predições/dados reais
pyplot.plot(segundoQuartil)
pyplot.plot(predicoes, color='red')
pyplot.show()
fim = time.time()

erro = "Erro de In em " + str(porcento*100)  +"%:\r\nValor Original: \tPrevisão: \t\tErro:\r\n"
i = 0
for e in S:
    erro+= str(e)+"\t\t\t"+str(predicoes[i])+"\t\t"+str(round(abs(100*(e/predicoes[i])),2)) + "%\r\n"
    i+=1
print(erro)
f = open("info.txt", "a")
f.write(str(predicoes) + "\r\n" + erro +"Tempo de execução: " + str(round(abs((inicio-fim)/60),0))+' mins')
f.close()
"""