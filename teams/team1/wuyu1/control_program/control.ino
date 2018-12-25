/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

#include <stdlib.h>
#include <string.h>
#define PIN_PUMP 13

int count1 = 0;
int count2 = 0;
int count3 = 0;
int threshold = 300;
int on_off = 0;
int input;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(PIN_PUMP,OUTPUT); 
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  long sensorValue = analogRead(A0);
  double water_sensorValue = (long)analogRead(A1);
  double depth = water_sensorValue/650*4;

  if (Serial.available()) {
    input = String(Serial.readString()).toInt(); 
    if (String(input).length() == 1) {
      on_off = input;
    }
    else {
      threshold = input;
    }
  }

  if (on_off == 0) {
    digitalWrite(PIN_PUMP,LOW);
    return;
  }
  
  // print out the value you read:
  Serial.print(sensorValue);
  Serial.print(" ");
  Serial.println(depth);
  
  if (sensorValue >= threshold) {
    count1 ++;
    count2 = 0;
  }
  else {
    count2 ++;
  }

  if (depth < 3.4) {
    count3 ++;
  }
  else {
    count3 = 0;
  }

  if (count1 >= 100) {
    digitalWrite(PIN_PUMP,HIGH);
  }

  if (count2 >= 20 || count3 >= 40) {
    digitalWrite(PIN_PUMP,LOW);
    count1 = 0;
  }
  
  delay(100);        // delay in between reads for stability
}
