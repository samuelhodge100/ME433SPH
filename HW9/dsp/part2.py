import matplotlib.pyplot as plt
import numpy as np
import csv

data1 = [] # column 0
data2 = [] # column 1
filt_data2 = []
filt_t = []
num_avg = 50
path = 'sigD.csv'
with open(path) as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one   
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column

# __fft
t = np.arange(0.0,data1[len(data1)-1]+data1[1],data1[1])

for i in range(num_avg-1,len(data1)):
    temp = 0
    for j in range(0,num_avg):
        temp += data2[i-j]
    filt_data2.append(temp/num_avg)
    filt_t.append(t[i])


Fs = 1/data1[1]# sample rate
Ts = data1[1]; # sampling interval
ts = np.arange(0,t[-1],Ts) # time vector     
y = filt_data2 # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq1 = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y1 = Y[range(int(n/2))]

Fs = 1/data1[1]# sample rate
Ts = data1[1]; # sampling interval
ts = np.arange(0,t[-1],Ts) # time vector     
y = data2 # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq2 = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y2 = Y[range(int(n/2))]


fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t,data2,'black')
ax1.plot(filt_t,filt_data2,'red')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq2,abs(Y2),'black')
ax2.loglog(frq1,abs(Y1),'red') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
fig.suptitle("Moving Average for "+str(path)+" ("+str(num_avg)+" data points)")
plt.show()
