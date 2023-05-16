import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('/dev/tty.usbmodem141101')
array = []
t = np.linspace(0,1024)

while(1):
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        array.append(decoded_bytes)
        
        if (len(array)>1024):
            print("Arrived")

            Fs = 1024 # sample rate
            y = array # the data to make the fft from
            n = len(y) # length of the signal
            k = np.arange(n)
            T = n/Fs
            frq = k/T # two sides frequency range
            frq = frq[range(int(n/2))] # one side frequency range
            Y = np.fft.fft(y)/n # fft computing and normalization
            Y = Y[range(int(n/2))]

            fig, (ax1, ax2) = plt.subplots(2, 1)
            fig.suptitle("FFT for data from PICO")
            ax1.plot(y,'b')
            ax1.set_xlabel('Time')
            ax1.set_ylabel('Amplitude')
            ax2.loglog(frq,abs(Y),'b') # plotting the fft
            ax2.set_xlabel('Freq (Hz)')
            ax2.set_ylabel('|Y(freq)|')
            # plt.plot(array)
            plt.show()
            ser.close()
            break
        

        print(len(array))
    except:
        print("Keyboard Interrupt")
        break


