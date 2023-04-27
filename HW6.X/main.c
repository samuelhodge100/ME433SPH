#include "i2c_master_noint.h"
#include "nu32dip.h"
#include <stdio.h>
#define WRITE_ADDY 0b01000000
#define READ_ADDY 0b01000001
#define OLAT_REG 0x0A
#define GPIO_REG 0x09
#define IODIR_REG 0x00


void generic_i2c_write(unsigned char address, unsigned char reg, unsigned char value);
int generic_i2c_read(unsigned char address_write, unsigned char address_read, unsigned char reg);

int main(void){
    // Initialize PIC and I2C
    NU32DIP_Startup();
    i2c_master_setup();
    // init the chip GP0 is input, GP7 is output
    generic_i2c_write(WRITE_ADDY,IODIR_REG,0b00000001);
    delay(0.1);
    
    while(1){
        NU32DIP_GREEN = 1;
        
        // send start bit
        // send address of the chip
            // TO WRITE: 0b01000000;  TO READ: 0b01000001
        // send the register name
            // 0x0A // OLAT
        // send the value to turn on GP7
            // 0b10000000
        // send stop bit
  
        
        int GP0 = generic_i2c_read(WRITE_ADDY,READ_ADDY,GPIO_REG);
        
        if(!GP0){
            generic_i2c_write(WRITE_ADDY,OLAT_REG,0b10000000);
        }else{
            generic_i2c_write(WRITE_ADDY,OLAT_REG,0b00000000); 
        }
        
        NU32DIP_GREEN = 0;
        
    }
    
    return 0;
}


void generic_i2c_write(unsigned char address, unsigned char reg, unsigned char value){
    i2c_master_start();
    i2c_master_send(address);
    i2c_master_send(reg);
    i2c_master_send(value);
    i2c_master_stop();
    
}

int generic_i2c_read(unsigned char address_write, unsigned char address_read, unsigned char reg){
    //send start bit
    i2c_master_start();
    //send address with write bit
    i2c_master_send(address_write);
    //send register you want to read from
    i2c_master_send(reg);
    //restart
    i2c_master_restart();
    //send address with read bit
    i2c_master_send(address_read);
    //recieve
    unsigned char r = i2c_master_recv();
    //send ackbit
    i2c_master_ack(1);
    //send stop
    i2c_master_stop();
    
    return(r&0b00000001);
}
