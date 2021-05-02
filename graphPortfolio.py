#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdate
from matplotlib import style
import numpy as np
# sys.path.insert(0,'/usr/local/lib/python3.7/site-packages/')

def readData(fileName):
    f = open(fileName, "r")
    data = eval(f.readline())
    prices = []
    time = []
    for first, second in data:
        prices.append(first)
        time.append(second)
    return prices, time

def graphDataFromFile(filename):
  data, time = readData(filename)
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
  global data, time, axis, fig
  data, time = readData(filename)
  # fig = plt.figure()
  fig, axis = plt.subplots()
  # axis = fig.add_subplot(1,1,1)
  ani = animation.FuncAnimation(fig, animate, interval=1000)
  plt.show()

def animate(i):
  axis.clear()
  # date_fmt = '%d-%m-%y %H:%M:%S'
  # date_formatter = mdate.DateFormatter(date_fmt)
  # axis.xaxis.set_major_formatter(date_formatter)
  # fig.autofmt_xdate()
  fmt = '${x",.0f}'
  axis.plot(time,data)


liveGraphDataFromFile("portfolioValues.txt")
