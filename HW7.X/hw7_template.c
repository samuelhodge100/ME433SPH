#include "nu32dip.h" // constants, functions for startup and UART
#include "i2c_master_noint.h"
#include "mpu6050.h"
#include <stdio.h>

void blink(int, int); // blink the LEDs function

int main(void) {
    NU32DIP_Startup(); // cache on, interrupts on, LED/button init, UART init
    init_mpu6050();     // calls 
	
    
	// char array for the raw data
    unsigned char d[14];
	// floats to store the data
    float ax,ay,az,gx,gy,gz,temp;

	// read whoami
    unsigned char iam = whoami();
	// print whoami
    char m_in[100];
    sprintf(m_in,"0x%X\r\n",iam);
    NU32DIP_WriteUART1(m_in);
	// if whoami is not 0x68, stuck in loop with LEDs on
    if(iam != 0x68){
        while(1){
            blink(1,5);
        }
    }
	// wait to print until you get a newline
    NU32DIP_ReadUART1(m_in,100);
    sprintf(m_in,"Newline reached");
    NU32DIP_WriteUART1(m_in);

    while (1) {
		// use core timer for exactly 100Hz loop
        _CP0_SET_COUNT(0);
        blink(1, 5);

        // read IMU
        burst_read_mpu6050(d);
		// convert data
        ax = conv_xXL(d);
        ay = conv_yXL(d);
        az = conv_zXL(d);
        gx = conv_xG(d);
        gy = conv_yG(d);
        gz = conv_zG(d);
        temp = conv_temp(d);
        
        // print out the data
        sprintf(m_in,"ax:%f\r\nay:%f\r\naz:%f\r\ngx:%f\r\ngy:%f\r\ngz:%f\r\ntemp:%f\r\n",ax,ay,az,gx,gy,gz,temp);
        NU32DIP_WriteUART1(m_in);
        
        while (_CP0_GET_COUNT() < 48000000 / 2 / 100) {
        }
    }
}

// blink the LEDs
void blink(int iterations, int time_ms) {
    int i;
    unsigned int t;
    for (i = 0; i < iterations; i++) {
        NU32DIP_GREEN = 0; // on
        NU32DIP_YELLOW = 1; // off
        t = _CP0_GET_COUNT(); // should really check for overflow here
        // the core timer ticks at half the SYSCLK, so 24000000 times per second
        // so each millisecond is 24000 ticks
        // wait half in each delay
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {
        }

        NU32DIP_GREEN = 1; // off
        NU32DIP_YELLOW = 0; // on
        t = _CP0_GET_COUNT(); // should really check for overflow here
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {
        }
    }
}

