import matplotlib.pyplot as plt
import numpy as np
import csv

data1 = [] # column 0
data2 = [] # column 1
filt_data2 = []
IIR_data2 = []
IIR_t = []
filt_t = []
num_avg = 47

h = [
    -0.000000000000000001,
    0.000064393676763220,
    0.000271319801257540,
    0.000649073204382278,
    0.001235623050647806,
    0.002076637553675906,
    0.003222058252059904,
    0.004721452177155942,
    0.006618513253826244,
    0.008945196904421814,
    0.011716041834802050,
    0.014923251981835048,
    0.018533075973444006,
    0.022483932798082779,
    0.026686597480116862,
    0.031026590809771163,
    0.035368727580917296,
    0.039563585562856544,
    0.043455480385182557,
    0.046891386356592825,
    0.049730143962839937,
    0.051851251307310706,
    0.053162553912562159,
    0.053606224358990776,
    0.053162553912562159,
    0.051851251307310706,
    0.049730143962839930,
    0.046891386356592839,
    0.043455480385182564,
    0.039563585562856544,
    0.035368727580917296,
    0.031026590809771187,
    0.026686597480116866,
    0.022483932798082775,
    0.018533075973443999,
    0.014923251981835051,
    0.011716041834802057,
    0.008945196904421819,
    0.006618513253826253,
    0.004721452177155945,
    0.003222058252059902,
    0.002076637553675908,
    0.001235623050647806,
    0.000649073204382280,
    0.000271319801257541,
    0.000064393676763220,
    -0.000000000000000001,
]

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
        temp += h[j]*data2[i-j]
    filt_data2.append(temp)
    filt_t.append(t[i])

Fs = 1/data1[1]# sample rate
print(Fs)
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
fig.suptitle("FIR for "+str(path)+" ("+str(num_avg)+" data points and number of coefficients "+str(len(h))+")")
plt.show()
