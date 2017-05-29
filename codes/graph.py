from matplotlib import pyplot
from csv import reader

import plotly.plotly as py
from plotly.graph_objs import *

with open('test.csv', 'r') as f:
    data = list(reader(f))

X = [int(i[1])/64 for i in data[1::]]
Y = [(int(j[3])/64)+20 for j in data[1::]]

a = X.index(30)

P = X[a:]
Q = Y[a:]

trace0 = Scatter(
    x= list(range(0,len(X))),
    y= X
)

data = Data([trace0])
#py.plot(data, filename = 'test')
pyplot.plot(range(len(P)), P)
pyplot.plot(range(len(Q)), Q)
pyplot.title('Measuring Instrumental Vibration')
pyplot.xlabel('Time axis')
pyplot.ylabel('Acceleration axis')
pyplot.show()
