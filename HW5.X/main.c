#include "nu32dip.h"
#include "spi.h"
#include <math.h>
#include <stdio.h>
#define NUMSAMPLES 100
#define CORETIMERTICKS 24000000


void makeSineWave(int* ptr);
void makeTriangleWave(int* ptr);
void delay(int t);



int main(void){
    // Initialize the PIC and SPI
    NU32DIP_Startup();
    initSPI();
    char message[100];
    
    // Pre-calculate voltages into arrays
    int Sinewave[NUMSAMPLES];
    int Trianglewave[NUMSAMPLES];
    makeSineWave(Sinewave);
    makeTriangleWave(Trianglewave);
    

    
    
    while(1){
        // Send voltage 2 Hrz sign wave for SPI
        //[a_or_b 1 1 1 [10bit voltagge] 0 0]
        
        
        unsigned short t = 0;
        int counttri = 0;
        int countsin = 0;
        
        for(int i=0; i<NUMSAMPLES; i++){
            // For the Sinewave 2 Hz
            _CP0_SET_COUNT(0);
            t = 0b0111<<12;
            t = t | (Sinewave[i]<<2);
            LATBbits.LATB13 = 0;
            spi_io(t>>8);
            spi_io(t);
            LATBbits.LATB13 = 1; 
            
            t = 0b1111<<12;
            t = t | (Trianglewave[i]<<2);
            LATBbits.LATB13 = 0;
            spi_io(t>>8);
            spi_io(t);
            LATBbits.LATB13 = 1;
            
            
             

            while(_CP0_GET_COUNT()<CORETIMERTICKS*0.005){
                ;
            }
            

        }

            
        
    }
    
    
    
    return 0;
}

void makeSineWave(int* ptr){
    for(int i=0; i<NUMSAMPLES; i++){
        ptr[i] = (int)(1023/2*(sin(2*i*3.1415/50)+1));  // 
    }
}

void makeTriangleWave(int* ptr){
    for(int i=0; i<NUMSAMPLES; i++){
        if(i<50){
            ptr[i] = (int)(20.9*i);
        }
        if(i>=50){
            ptr[i] = (int)(-20.9*i+2048.2);
        }
    }    
}

void delay(int t){
    _CP0_SET_COUNT(0);
    while(_CP0_GET_COUNT()<CORETIMERTICKS*t){
        ;
    }
    
}