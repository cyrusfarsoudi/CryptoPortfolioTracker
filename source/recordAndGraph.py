import threading
import crypto
import graphPortfolio

def runCrypto():
  crypto.Asset.buildApiObjects()
  portfolio = crypto.readPortfolioYaml("data/portfolio.yaml")
  crypto.watchPortfolio(portfolio)

def runGraphPortfolio():
  graphPortfolio.liveGraphDataFromFile("data/portfolioValues.dat")

t1 = threading.Thread(target=runCrypto)
t1.start()
runGraphPortfolio()
