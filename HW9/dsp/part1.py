import matplotlib.pyplot as plt
import numpy as np
import csv

data1 = [] # column 1
data2 = [] # column 2

with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one   
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column

# __fft
t = np.arange(0.0,data1[len(data1)-1]+data1[1],data1[1])
Fs = 1/data1[1]# sample rate
Ts = data1[1]; # sampling interval
ts = np.arange(0,t[-1],Ts) # time vector     
y = data2 # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t,y,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq,abs(Y),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()

plt.show()