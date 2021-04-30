#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, time
import ccxt

coinbase = ccxt.coinbase()
binanceus = ccxt.binanceus()
kraken = ccxt.kraken()

class Asset:
  def __init__(self, name, exchange, quantity, costBasis=0):
    self.name = name
    self.exchange = exchange
    self.quantity = quantity
    self.costBasis = costBasis
    self.lastPrice = 0

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

assets = []
assets.append(Asset("BTC", coinbase, .01162942))
assets.append(Asset("ETH", coinbase, .28618991))
assets.append(Asset("ADA", kraken, 163.3))
assets.append(Asset("DOGE", kraken, 533.9))
assets.append(Asset("VET", binanceus, 919.3))

def writeToFile(fileName, data):
  f = open(fileName, 'w')
  f.write(data)
  f.close()


def recordPortfolioStats():
  history = []
  iterations = 0
  print("Total Portfolio Value: ")
  while(True):
    iterations = iterations + 1
    totalValue = 0
    for asset in assets:
      asset.getCurrentPrice()
      totalValue = totalValue + asset.getCurrentValue()
    history.append((totalValue, time.time()))
    if(iterations % 50 == 0):
      writeToFile("portfolioValues.txt", str(history))
    print(totalValue,end='\r')

recordPortfolioStats()
