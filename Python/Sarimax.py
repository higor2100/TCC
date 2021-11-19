import pandas
from statsmodels.tsa.arima.model import ARIMA
df = pandas.read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")
# 1,1,2 ARIMA Model
model = ARIMA(df['bytes'], order=(1,0,0))
model_fit = model.fit()
print(model_fit.summary())

