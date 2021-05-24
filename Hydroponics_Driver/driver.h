#include "driver.h"

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