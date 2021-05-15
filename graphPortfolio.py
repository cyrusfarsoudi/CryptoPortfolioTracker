#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
import matplotlib.dates as mdate
from matplotlib import style
import numpy as np

import crypto
# sys.path.insert(0,'/usr/local/lib/python3.7/site-packages/')

def readHistoricalData(fileName):
  f = open(fileName, "r")
  data = eval(f.readline())
  prices = []
  time = []
  for first, second in data:
      prices.append(first)
      time.append(second)
  return prices, time

def readData(fileName):
  f = open(fileName, "r")
  return eval(f.readline())

def graphDataFromFile(filename):
  data, time = readHistoricalData(filename)
  secs = mdate.epoch2num(time)
  fig, axis = plt.subplots()
# Plot the date using plot_date rather than plot
  axis.plot_date(secs, data)
  plt.plot(secs,data)
# Choose your xtick format string
  date_fmt = '%d-%m-%y %H:%M:%S'
# Use a DateFormatter to set the data to the correct format.
  date_formatter = mdate.DateFormatter(date_fmt)
  axis.xaxis.set_major_formatter(date_formatter)
# Sets the tick labels diagonal so they fit easier.
  fig.autofmt_xdate()
  plt.show()

def liveGraphDataFromFile(filename):
  global axis, fig, dataFile
  dataFile = filename
  fig, axis = plt.subplots()
  ani = animation.FuncAnimation(fig, animate, interval=1000)
  plt.show()

def makeLegend(portfolio):
  colors = ["yellow", "blue", "orange", "purple", "red"]
  mp = []
  for key in portfolio:
    mp.append(mpatches.Patch(color=colors.pop(), label=(key.name + ": " + str(round(lastPrices[key.name],2)) + " (" + str(round(lastValues[key.name],2)) + ")")))
  return mp

def animate(i):
  data, time = readHistoricalData(dataFile)
  global lastPrices, lastValues
  lastPrices = readData("lastPrices.txt")
  lastValues = readData("lastValues.txt")
  data = data[-10000:]
  time = time[-10000:]
  secs = mdate.epoch2num(time)
  axis.clear()

  date_fmt = '%d-%m-%y %H:%M:%S'
  date_formatter = mdate.DateFormatter(date_fmt)
  axis.xaxis.set_major_formatter(date_formatter)
  fig.autofmt_xdate()
  axis.plot(secs,data)

  plt.legend(handles=makeLegend(portfolio))

  totalValue = 0
  for value,key in lastValues.items():
    totalValue = totalValue + key
  plt.title("Total Portfolio Value: " + str(round(totalValue,2)))

portfolio = crypto.readPortfolioYaml("portfolio.yaml", False)
liveGraphDataFromFile("portfolioValues.txt")
