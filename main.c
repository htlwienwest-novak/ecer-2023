#include <kipr/wombat.h>

int hellDunkelLinks = 0; // 1 = weiss, 0 = schwarz
int hellDunkelRechts = 0;
int schwellenwert = 3300;

int main()
{	    
    while (1)
    {
        //int abstandsSensor = analog(0);
    	//printf("Abstand: %d\n", abstandsSensor);
    
        int farbSensorLinks = analog(1);
        int farbSensorRechts = analog(2);

        if (farbSensorLinks < schwellenwert)
        {
            hellDunkelLinks = 1;
        }
        else 
        {
            hellDunkelLinks = 0;
        }
        
        if (farbSensorRechts < schwellenwert)
        {
            hellDunkelRechts = 1;
        }
        else 
        {
            hellDunkelRechts = 0;
        }
        
        if (hellDunkelLinks && hellDunkelRechts) 
        {
            printf("weiss links: %d, rechts: %d\n", farbSensorLinks, farbSensorRechts); 
        }
        else 
        {
            printf("weiss links: %d, rechts: %d\n", farbSensorLinks, farbSensorRechts);
        }

        if(hellDunkelLinks && hellDunkelRechts)
        {
            motor(0,100);
            motor(1,100);
        }
        else if (!hellDunkelLinks && hellDunkelRechts)
        {
            motor(0,-20);
            motor(1,100);
            msleep(5);
        }
        else if (hellDunkelLinks && !hellDunkelRechts)
        {
            motor(0,100);
            motor(1,-20);
            msleep(5);
        }
        else if (!hellDunkelLinks && !hellDunkelRechts)
        {
            motor(0,100);
            motor(1,100);
        }  
    }
}
