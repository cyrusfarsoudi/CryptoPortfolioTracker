#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, matplotlib.pyplot as plt

def readData(fileName):
    f = open(fileName, "r")
    return eval(f.readline())

data = readData("portfolioValues.txt")

plt.plot(data)
plt.show()
