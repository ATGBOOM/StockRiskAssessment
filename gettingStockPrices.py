import requests
import matplotlib.pyplot as plt

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=86RBOQWSMRRCBOWX'
r = requests.get(url)
dat = r.json()
print(dat)
dataDates = list(dat['Monthly Time Series'].keys())
dataVals = list(dat['Monthly Time Series'].values())

data = []

for i in range(50):
    data.append([dataDates[i], (float(dataVals[i]['2. high']) + float(dataVals[i]['3. low'])) / 2 ])


