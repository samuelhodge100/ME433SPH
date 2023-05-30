#include "nu32dip.h"
#include <stdio.h>

int main(){
    NU32DIP_Startup();
    
    // Setup
    RPA0Rbits.RPA0R = 0b0101;    // Set pin A0 as PWM output pin
    T3CONbits.TCKPS = 6;        // Timer3 prescaler 1:64
    PR3 = 15000-1;               // period = (PR2+1) * N * 12.5 ns = 100 us, 10 kHz
    TMR3 = 0;                   // initial TMR2 count is 0
    OC1CONbits.OCM = 0b110;     // PWM mode without fault pin; other OC1CON bits are defaults
    OC1CONbits.OCTSEL = 1;      // Set timer 3 to be used with comparison
    OC1RS = 1000;                  // duty cycle = OC1RS/(PR3+1) = 25%
    OC1R = 0;                    // initialize before turning OC1 on; afterward it is read-only
    T3CONbits.ON = 1;              // turn on Timer3
    OC1CONbits.ON = 1;             // turn on OC1
    
    while(1){
    
    OC1RS = 1000;
    delay(2);
    OC1RS = 2000;
    delay(2);
 
    }
    
    
}

