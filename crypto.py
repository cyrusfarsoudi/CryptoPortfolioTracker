#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, time
sys.path.insert(0,'/usr/local/lib/python3.7/site-packages/')
import ccxt, yaml

coinbase = ccxt.coinbase()
binanceus = ccxt.binanceus()
kraken = ccxt.kraken()

class Asset:
  def __init__(self, name, exchange, quantity, costBasis=0):
    self.name = name
    self.exchange = Asset.fetchApiObject(exchange)
    self.quantity = quantity
    self.costBasis = costBasis
    self.lastPrice = 0

  def buildApiObjects():
    Asset.coinbase = ccxt.coinbase()
    Asset.binanceus = ccxt.binanceus()
    Asset.kraken = ccxt.kraken()

  def fetchApiObject(exchange):
    if(exchange == "coinbase"):
      return Asset.coinbase
    if(exchange == "binanceus"):
      return Asset.binanceus
    if(exchange == "kraken"):
      return Asset.kraken

  def getCurrentPrice(self):
    self.lastPrice = self.exchange.fetch_ticker(self.name + "/USD")['last']
    return self.lastPrice

  def getCurrentValue(self):
    if(not self.lastPrice):
      self.getCurrentPrice()
    self.lastValue = self.lastPrice * self.quantity
    return self.lastValue

  def printPrice(self):
    if(not self.lastPrice):
      self.getCurrentPrice()
    print(self.name + ": " + str(self.lastPrice))

Asset.buildApiObjects()

def readPortfolioYaml(fileName):
  with open(fileName, "r") as stream:
    try:
      data =  yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
  portfolio = []
  for key, val in data.items():
    portfolio.append(Asset(key, val["exchange"], val["quantity"]))
  return portfolio

def writeToFile(fileName, data):
  f = open(fileName, 'w')
  f.write(data)
  f.close()

def recordPortfolioStats(portfolio):
  history = []
  iterations = 0
  print("Total Portfolio Value: ")
  while(True):
    iterations = iterations + 1
    totalValue = 0
    try:
      for asset in portfolio:
        asset.getCurrentPrice()
        totalValue = totalValue + asset.getCurrentValue()
    except:
      continue
    history.append((totalValue, time.time()))
    if(iterations % 30 == 0):
      writeToFile("portfolioValues.txt", str(history))
    print(totalValue,end='\r')

portfolio = readPortfolioYaml("portfolio.yaml")
recordPortfolioStats(portfolio)
