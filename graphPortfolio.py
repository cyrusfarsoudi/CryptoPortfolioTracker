#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, matplotlib.pyplot as plt

import matplotlib.dates as mdate
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


data, time = readData("portfolioValues.txt")
secs = mdate.epoch2num(time)

fig, ax = plt.subplots()

# Plot the date using plot_date rather than plot
# ax.plot_date(secs, data)
plt.plot(secs,data)

# Choose your xtick format string
date_fmt = '%d-%m-%y %H:%M:%S'

# Use a DateFormatter to set the data to the correct format.
date_formatter = mdate.DateFormatter(date_fmt)
ax.xaxis.set_major_formatter(date_formatter)

# Sets the tick labels diagonal so they fit easier.
fig.autofmt_xdate()

plt.show()

# plt.plot(secs, data)
# plt.show()
