#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, time
import ccxt, yaml
from EpochPST import EpochPST

coinbase = ccxt.coinbase()
binanceus = ccxt.binanceus()
kraken = ccxt.kraken()

class Asset:
  def __init__(self, name, exchange, quantity, costBasis=0, setupApi=True):
    self.name = name
    self.quantity = quantity
    self.costBasis = costBasis
    self.lastPrice = 0
    if(setupApi):
      self.exchange = Asset.fetchApiObject(exchange)

  def buildApiObjects():
    Asset.coinbase = ccxt.coinbase()
    Asset.binanceus = ccxt.binanceus()
    Asset.kraken = ccxt.kraken()
    Asset.apiObjectsBuilt = True

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

  def getCurrentProfit(self):
    return self.getCurrentValue() - self.costBasis * self.quantity

  def printPrice(self):
    if(not self.lastPrice):
      self.getCurrentPrice()
    print(self.name + ": " + str(self.lastPrice))


def readPortfolioYaml(fileName, buildApi=True):
  if(buildApi):
    Asset.buildApiObjects()
  with open(fileName, "r") as stream:
    try:
      data =  yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
  portfolio = []
  for key, val in data.items():
    portfolio.append(Asset(key, val["exchange"], val["quantity"], val["costBasis"], buildApi))
  return portfolio

def writeToFile(fileName, data):
  f = open(fileName, 'w')
  f.write(data)
  f.close()

def watchPortfolio(portfolio):
  history = []
  lastPrices = {}
  lastValues = {}
  lastProfits = {}
  iterations = 0
  lastTotal = 0
  print("Total Portfolio Value: ")
  while(True):
    iterations = iterations + 1
    totalValue = 0
    try:
      for asset in portfolio:
        lastPrices[asset.name] = asset.getCurrentPrice()
        lastValues[asset.name] = asset.getCurrentValue()
        lastProfits[asset.name] = asset.getCurrentProfit()
        totalValue = totalValue + asset.getCurrentValue()
    except Exception as e:
      print(e)
      continue
    if(totalValue == lastTotal):
      continue
    else:
      lastTotal = totalValue
    history.append((totalValue, EpochPST.getPST()))
    writeToFile("portfolioValues.txt", str(history))
    writeToFile("lastPrices.txt", str(lastPrices))
    writeToFile("lastValues.txt", str(lastValues))
    writeToFile("lastProfits.txt", str(lastProfits))
    print(totalValue,end='\r')


def main():
  Asset.buildApiObjects()
  portfolio = readPortfolioYaml("portfolio.yaml")
  watchPortfolio(portfolio)

if __name__ == "__main__":
    main()
