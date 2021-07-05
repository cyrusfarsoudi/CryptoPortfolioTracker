import pickle

def writeData(fileName, data):
  with open(fileName, 'w') as f:
    f.write(data)

def readData(fileName):
  with open(fileName, 'w') as f:
    return eval(f.readline())

def writeBinaryData(filename, data):
  with open(filename, 'wb') as f:
    pickle.dump(data, f)

def readBinaryData(filename):
  with open(filename, 'rb') as f:
    return pickle.load(f)