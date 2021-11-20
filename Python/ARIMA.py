# evaluate an ARIMA model using a walk-forward validation
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import time
import os

inicio = time.time()

df = read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")
#parse_dates=True, squeeze=True, date_parser=parser)
# split into train and test sets
X = df['bytes']
X.drop(X.tail(5).index,inplace=True)
size = int(len(X) * 0.5)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
# walk-forward validation
for t in test: 
    model = ARIMA(history, order=(1,0,0))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = int(output[0])
    predictions.append(yhat)
    obs = int(t)
    history.append(obs)
# evaluate forecasts
rmse = sqrt(mean_squared_error(test, predictions))
print('Teste do RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
fim = time.time()
f = open("info.txt", "a")
f.write(str(test) +"\r\n"+ str(predictions) + "\r\n" + "Tempo de execução:" + str(round((inicio-fim)/60,0))+' mins')
f.close()
#os.system("shutdown /s /t 1")