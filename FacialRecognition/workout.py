import numpy
fw = open('td.txt', 'r+')
data = eval(fw.read())
data=numpy.mean(data)
print(data)