import matplotlib.pyplot as plt
import numpy as np
import csv

data1 = [] # column 0
data2 = [] # column 1
filt_data2 = []
IIR_data2 = []
IIR_t = []
filt_t = []
num_avg = 93

h = [
    0.000000000000000000,
    0.000000000000000000,
    -0.000011630407605336,
    -0.000016685876162815,
    0.000030714762043070,
    0.000080677137832956,
    0.000000000000000000,
    -0.000172259750367664,
    -0.000145716933132334,
    0.000193698589739695,
    0.000407178976551273,
    -0.000000000000000001,
    -0.000652330200285278,
    -0.000499944562009187,
    0.000613150407171976,
    0.001205088560750828,
    -0.000000000000000002,
    -0.001734906421864614,
    -0.001272953023212590,
    0.001501963522563159,
    0.002851427247674092,
    -0.000000000000000004,
    -0.003867678382179018,
    -0.002765788759986591,
    0.003188024725914361,
    0.005925579956551043,
    -0.000000000000000007,
    -0.007752197536804714,
    -0.005460989694228917,
    0.006213796521650214,
    0.011426132137987179,
    -0.000000000000000010,
    -0.014737544197304983,
    -0.010351779338073271,
    0.011784290468445067,
    0.021765669641354731,
    -0.000000000000000013,
    -0.028768617695195800,
    -0.020674619573705581,
    0.024324730749154904,
    0.047085117073133585,
    -0.000000000000000015,
    -0.073397829386347938,
    -0.061300551078186820,
    0.092835555199572942,
    0.302151635285898779,
    0.399999183705328054,
    0.302151635285898779,
    0.092835555199572956,
    -0.061300551078186820,
    -0.073397829386347938,
    -0.000000000000000015,
    0.047085117073133578,
    0.024324730749154904,
    -0.020674619573705588,
    -0.028768617695195797,
    -0.000000000000000013,
    0.021765669641354735,
    0.011784290468445067,
    -0.010351779338073273,
    -0.014737544197304983,
    -0.000000000000000010,
    0.011426132137987190,
    0.006213796521650211,
    -0.005460989694228918,
    -0.007752197536804716,
    -0.000000000000000007,
    0.005925579956551046,
    0.003188024725914359,
    -0.002765788759986593,
    -0.003867678382179019,
    -0.000000000000000004,
    0.002851427247674094,
    0.001501963522563160,
    -0.001272953023212590,
    -0.001734906421864614,
    -0.000000000000000002,
    0.001205088560750829,
    0.000613150407171977,
    -0.000499944562009187,
    -0.000652330200285277,
    -0.000000000000000001,
    0.000407178976551273,
    0.000193698589739695,
    -0.000145716933132334,
    -0.000172259750367663,
    0.000000000000000000,
    0.000080677137832956,
    0.000030714762043070,
    -0.000016685876162815,
    -0.000011630407605336,
    0.000000000000000000,
    0.000000000000000000,
]

path = 'sigA.csv'

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
fig.suptitle("FIR for "+str(path)+" ("+str(num_avg)+" data points and number of coefficients "+str(len(h))+")")
plt.show()
