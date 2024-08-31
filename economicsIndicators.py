import requests
url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=86RBOQWSMRRCBOWX'
r = requests.get(url)
gdp = r.json()

url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=86RBOQWSMRRCBOWX'
r = requests.get(url)
ir = r.json()

url = 'https://www.alphavantage.co/query?function=INFLATION&apikey=86RBOQWSMRRCBOWX'
r = requests.get(url)
inflation = r.json()

