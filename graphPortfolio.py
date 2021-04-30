#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import sys, matplotlib.pyplot as plt
sys.path.insert(0,'/usr/local/lib/python3.7/site-packages/')

def readData(fileName):
    f = open(fileName, "r")
    return eval(f.readline())

data = readData("portfolioValues.txt")

plt.plot(data)
plt.show()

# x axis values
# x = [1,2,3]
# # corresponding y axis values
# y = [2,4,1]
  
# # plotting the points 
# plt.plot(x, y)

# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
  
# # giving a title to my graph
# plt.title('My first graph!')
  
# # function to show the plot
# plt.show()