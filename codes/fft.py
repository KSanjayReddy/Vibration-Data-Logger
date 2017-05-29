from matplotlib import pyplot

#import matplotlib.pyplot as plt
#import plotly.plotly as py
import numpy as np
from csv import reader

with open('test.csv', 'r') as f:
    data = list(reader(f))


x1 = [int(i[1])/64 for i in data[1::]]
x2 = [(int(j[3])/64)+20 for j in data[1::]]

a = x1.index(max(x1))
y1 = x1[a:]
y2 = x2[a:]

t1= list(range(0,len(y1)))
t2= list(range(0,len(y2)))
#y = [(int(j[3])/64)+20 for j in data[1::]]

Fs = 150.0;  # sampling rate

n1 = len(y1) # length of the signal
k1 = np.arange(n1)
T1 = n1/Fs
frq1 = k1/T1 # two sides frequency range
frq1 = frq1[range(n1/2)] # one side frequency range
Y1 = np.fft.fft(y1)/n1 # fft computing and normalization
Y1 = Y1[range(n1/2)]

n2 = len(y2) # length of the signal
k2 = np.arange(n2)
T2 = n2/Fs
frq2 = k2/T2 # two sides frequency range
frq2 = frq2[range(n2/2)] # one side frequency range
Y2 = np.fft.fft(y2)/n2 # fft computing and normalization
Y2 = Y2[range(n2/2)]


pyplot.subplot(211)
pyplot.plot(t1,y1)
pyplot.plot(t2,y2)

pyplot.subplot(212)
pyplot.plot(frq1,abs(Y1))
pyplot.plot(frq1,abs(Y2))
pyplot.show()

#fig, ax = plt.subplots(2, 1)
#ax[0].plot(t,y)
#ax[0].set_xlabel('Time')
#ax[0].set_ylabel('Amplitude')
#ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
#ax[1].set_xlabel('Freq (Hz)')
#ax[1].set_ylabel('|Y(freq)|')

#plot_url = py.plot_mpl(fig, filename='test')
