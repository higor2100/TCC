#############################################
#  Grid Search ARIMA model hyperparameters  #
#############################################
#
# from Brownlee, Jason - "Introduction to time series forecasting with Python"
#
import warnings
from pandas import read_csv
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot


warnings.filterwarnings("ignore")

# evaluate an ARIMA model for a given order (p,d,q)


def arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X)*0.9999)
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
    return predictions
# load dataset
df = read_csv('C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\PACS01 - Trafego Out VDX PACS01_To_CORE02.csv', sep=",")

#leitura e remoção de dados do arquivo csv
tabela = df['bits']

# evaluate parameters
predicao = arima_model(tabela.head(len(tabela)-6), (1,0,3))

ax = list(range(len(tabela)+len(predicao)))
#pyplot.plot(ax[len(tabela)-50:len(tabela)],tabela[ax[len(tabela)-50:len(tabela)]],color='red')
pyplot.plot(ax[0:len(tabela)],tabela,color='red')
pyplot.plot(ax[len(tabela):],predicao,color='green')
pyplot.show()