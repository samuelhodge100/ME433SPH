#include <stdio.h>
#include "font.h"
#include "nu32dip.h"
#include "ssd1306.h"
#include <string.h>
#include "mpu6050.h"

void drawChar(unsigned char x, unsigned char y, unsigned char letter);
void drawString(unsigned char x, unsigned char y, char* m);

int main(void){
    NU32DIP_Startup();
    i2c_master_setup();
    ssd1306_setup();
    init_mpu6050();
    
    // char array for the raw data
    unsigned char d[14];
	// floats to store the data
    float ax,ay,az,gx,gy,gz,temp;
    
    unsigned char iam = whoami();
    
    if(iam != 0x68){
        while(1){
            ;
        }
    }
    
    
    char m[100];
    sprintf(m,"Initialization Complete\r\n");
    NU32DIP_WriteUART1(m);
    
    while(1){
        _CP0_SET_COUNT(0);
        NU32DIP_YELLOW = 0;
        NU32DIP_GREEN = 1;
        
        // read IMU
        burst_read_mpu6050(d);
		// convert data tp float
        ax = conv_xXL(d);
        ay = conv_yXL(d);
        az = conv_zXL(d);
        gx = conv_xG(d);
        gy = conv_yG(d);
        gz = conv_zG(d);
        temp = conv_temp(d);
        
        
        sprintf(m,"Z Accel: %.4f", az);
        
        drawString(10,10,m);
        
        sprintf(m,"FPS: %.2f",1/(_CP0_GET_COUNT()/24000000.0));
        drawString(10,20,m);
        
        
        while(_CP0_GET_COUNT()<((int)(24000000*.5))){
            ;
        }
        
        ssd1306_clear();

        NU32DIP_YELLOW = 1;
        NU32DIP_GREEN = 0;
    }
}


void drawChar(unsigned char x, unsigned char y, unsigned char letter){
    for(unsigned char i=0; i<5; i++){
        for(unsigned char j=0; j<8;j++){
            
            if((((ASCII[letter-0x20][i]>> j) & 0b1)) == 0b1){
                ssd1306_drawPixel(x+i,y+j,1);
            }
        }
    }
    ssd1306_update();
}

void drawString(unsigned char x, unsigned char y, char* m){
    // Check to make sure there is no over flow
    unsigned char x_ind;
    unsigned char y_ind;
    for(unsigned char i=0; i<strlen(m);i++){
        x_ind = x+5*i;
        y_ind = y;
        
      
        drawChar(x_ind,y_ind,m[i]);
        
    }
}