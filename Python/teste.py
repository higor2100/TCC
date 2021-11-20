import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\higor\\Documents\\GitHub\\TCC\\Jupyter\\Arquivo CSV\\PACS01 - Trafego In VDX PACS01_To_CORE02.csv", sep=",")
df.head()

# Updating the header
df.head()
df.describe()
df.set_index('time',inplace=True)

from pylab import rcParams
rcParams['figure.figsize'] = 200, 50
df.plot()

from statsmodels.tsa.stattools import adfuller
test_result=adfuller(df['bytes'])

def adfuller_test(bytes):
    result=adfuller(bytes)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )

    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data is stationary")
    else:
        print("weak evidence against null hypothesis,indicating it is non-stationary ")

adfuller_test(df['bytes'])

df['bytes First Difference'] = df['bytes'] - df['bytes'].shift(1)
df['Seasonal First Difference']=df['bytes']-df['bytes'].shift(1000)
df.head()

# Again testing if data is stationary
adfuller_test(df['Seasonal First Difference'].dropna())
#df['Seasonal First Difference'].plot()
from pandas.plotting import autocorrelation_plot
#autocorrelation_plot(df['bytes'])
#plt.show()
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.api as sm
"""
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df['Seasonal First Difference'].dropna(),lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df['Seasonal First Difference'].dropna(),lags=40,ax=ax2)
"""
from statsmodels.tsa.arima_model import ARIMA
model=ARIMA(df['bytes'],order=(1,0,0))
model_fit=model.fit(disp=0)
print(model_fit.summary())
df['forecast']=model_fit.predict(start=48999,end=49999,dynamic=True)
#df[['bytes','forecast']].plot(figsize=(12,8))

import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df['bytes'],order=(1, 0, 0), seasonal_order=(1,0,0,1000))
results=model.fit(disp=0)
df['forecast']=results.predict(start=48999,end=49999,dynamic=True)
#df[['bytes','forecast']].plot(figsize=(12,8))


df['forecast'].plot(figsize=(200, 50))