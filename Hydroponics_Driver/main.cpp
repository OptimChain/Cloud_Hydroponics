/**********************************************************

Connect the red wire to +5V, 
the black wire to common ground 
and the yellow sensor wire to pin #2


**********************************************************/
#include <iostream>		// Include all needed libraries here
#include <wiringPi.h>
#include "driver.h"

using namespace std;
		// No need to keep using “std”

// which pin to use for reading the sensor? can use any pin!
#define FLOWSENSORPIN 2

// count how many pulses!
volatile uint16_t pulses = 0;
// track the state of the pulse pin
volatile uint8_t lastflowpinstate;
// you can try to keep time of how long it is between pulses
volatile uint32_t lastflowratetimer = 0;
// and use that to calculate a flow rate
volatile float flowrate;

namespace functions {

void setup() {

   cout << "Flow sensor test!";
   
   pinMode(FLOWSENSORPIN, INPUT);
   lastflowpinstate = digitalRead(FLOWSENSORPIN);
}

void loop()                     // run over and over again
{ 

  // lambda to read code
  []() {

     uint8_t x = digitalRead(FLOWSENSORPIN);
  
  if (x == lastflowpinstate) {
    lastflowratetimer++;
    return; // nothing changed!
  }
  
  if (x == HIGH) {
    //low to high transition!
    pulses++;
  }
  lastflowpinstate = x;
  flowrate = 1000.0;
  flowrate /= lastflowratetimer;  // in hertz
  lastflowratetimer = 0;


  };
  cout << "Pulses:"; cout << pulses;
  cout << " Hz:";
  cout << flowrate;
  //print(flowrate);
  cout << "Freq: "; cout << flowrate;
  cout << "Pulses: "; cout << pulses;
  
  //if a plastic sensor use the following calculation
  //Sensor Frequency (Hz) = 7.5 * Q (Liters/min)
  // Liters = Q * time elapsed (seconds) / 60 (seconds/minute)
  // Liters = (Frequency (Pulses/second) / 7.5) * time elapsed (seconds) / 60
  // Liters = Pulses / (7.5 * 60)
  float liters = pulses;
  liters /= 7.5;
  liters /= 60.0;

/*
  // if a brass sensor use the following calculation
  float liters = pulses;
  liters /= 8.1;
  liters -= 6;
  liters /= 60.0;
*/
  cout << liters; cout << " Liters";
  // lambda to read code
  []() {

     uint8_t x = digitalRead(FLOWSENSORPIN);
  
  if (x == lastflowpinstate) {
    lastflowratetimer++;
    return; // nothing changed!
  }
  
  if (x == HIGH) {
    //low to high transition!
    pulses++;
  }
  lastflowpinstate = x;
  flowrate = 1000.0;
  flowrate /= lastflowratetimer;  // in hertz
  lastflowratetimer = 0;


  };
  cout << liters; cout << " Liters";
  
  
  delay(100);
}
} 
 
int main()
{
    wiringPiSetup();			// Setup the library
    pinMode(0, OUTPUT);		// Configure GPIO0 as an output
    pinMode(1, INPUT);		// Configure GPIO1 as an input

// Interrupt is called once a millisecond, looks for any pulses from the sensor!
 //Configure GPIO pins
 setup();
 //Loop Sensor Values
 loop();
 
}
 
 
