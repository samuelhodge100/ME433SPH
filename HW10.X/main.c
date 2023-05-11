#include "nu32dip.h"
#include "ws2812b.h"
#include <stdio.h>

int main(){
    NU32DIP_Startup();
    ws2812b_setup();
  
    while(1){
        wsColor c[6];
        for(int i=0; i<360; i++){ 
            c[0] = HSBtoRGB(i, 1.0, 1.0);
            c[1] = HSBtoRGB(i, 1.0, 1.0);
            c[2] = HSBtoRGB(i, 1.0, 1.0);
            ws2812b_setColor(c, 3);
            delay(0.1);
    }
        
    }
}
