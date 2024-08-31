import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf


stocks = ['BNS.TO', 'GOOGL', 'XOM']

data = yf.Ticker('GOOGL')
hisData = data.history(period='10y', interval='3mo')
hisData = hisData['Close']

prev = 0
change = []
for i in range(3, len(hisData) - 1, 4):

    change.append((hisData.iloc[i] - hisData.iloc[prev])/hisData.iloc[prev])
    prev = i + 1
expectedReturn = sum(change)*100/len(change)
expectedVar = sum([((x*100 - expectedReturn) ** 2)
                  for x in change]) / len(change)
stdev = expectedVar**0.5
S0 = hisData.iloc[len(hisData) - 1]
mean = expectedReturn/100
stdev = stdev/100
T = 1/365


print(expectedReturn)
paths = 100
n = 1
dt = T/n
plt.figure(figsize=(17, 10))
newstock = [S0]
predictedReturn = []

for j in range(paths):
    newstock = [S0]
    count = 0
    for i in range(365*5-1):

        if count > 365:
            predictedReturn.append(
                (newstock[i]-newstock[i-365])*100/newstock[0])
            count = 0
        newstock.append(newstock[-1]*(1 + mean*dt +
                        stdev*np.random.randn()*dt**0.5))
        count += 1
    plt.plot([i for i in range(365*5)], newstock)
plt.show()

predictedChange = sum(predictedReturn)/len(predictedReturn)
print(predictedChange)
