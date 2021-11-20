from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import time

inicio = time.time()

#criação do dataframe
df = read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")

#leitura e remoção de dados do arquivo csv
X = df['bytes']
X.drop(X.tail(5).index,inplace=True)

tamanho = int(len(X) * 0.5)
treino, teste = X[0:tamanho], X[tamanho:len(X)]
historico = [x for x in treino]
predicoes = list()
#criação do modelo
for t in teste: 
    modelo = ARIMA(historico, order=(1,0,0))
    modelo_fit = modelo.fit()
    saida = modelo_fit.forecast()
    yhat = int(saida[0])
    predicoes.append(yhat)
    obs = int(t)
    historico.append(obs)
    
# Teste RMSE com as predições
rmse = sqrt(mean_squared_error(teste, predicoes))
print('Teste do RMSE: %.3f' % rmse)

# plot das predições/dados reais
pyplot.plot(teste)
pyplot.plot(predicoes, color='red')
pyplot.show()
fim = time.time()

f = open("info.txt", "a")
f.write(str(teste) +"\r\n"+ str(predicoes) + "\r\n" + "Tempo de execução:" + str(round((inicio-fim)/60,0))+' mins')
f.close()