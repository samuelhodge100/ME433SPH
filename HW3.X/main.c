#include <stdio.h>
#include "nu32dip.h"
#include <math.h>
#include <string.h>
#define CORETIMERTICKS 24000000

float waveform[100];
void makeWaveform(float *ptr);
void delay(int t);

int main(void){
    char message[100];
    NU32DIP_Startup();
    makeWaveform(waveform);
    
   
    while(1){
        if(!NU32DIP_USER){
             for (int i=0; i<100; i++){
                sprintf(message,"%f\r\n",waveform[i]);
                NU32DIP_WriteUART1(message);
                delay(0.01);                                                    // Delay for 0.01 seconds
            }
            
        }
        
    }
    
}

void makeWaveform(float  *waveform){
    for(int i=0; i<100; i++){
        waveform[i] = sin(i*3.14/50.0);
    }
}

void delay(int t){
    _CP0_SET_COUNT(0);
    while(_CP0_GET_COUNT()<CORETIMERTICKS*t){
        ;
    }
    
}