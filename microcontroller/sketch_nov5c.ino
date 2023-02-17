/*
 [amazon &title=HC-SR04&text=HC-SR04] Ping distance sensor:
 VCC to arduino 5v 
 GND to arduino GND
 Echo to Arduino pin 7 
 Trig to Arduino pin 8
 
 This sketch originates from Virtualmix: http://goo.gl/kJ8Gl
 Has been modified by Winkle ink here: http://winkleink.blogspot.com.au/2012/05/arduino-hc-sr04-ultrasonic-distance.html
 And modified further by ScottC here: http://arduinobasics.blogspot.com.au/2012/11/arduinobasics-hc-sr04-ultrasonic-sensor.html
 on 10 Nov 2012.
 https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody
 */

 #include "pitches.h"

int RXLED = 17; // The RX LED has a defined Arduino pin
int TXLED = 30; // The TX LED has a defined Arduino pin

#define echoPin 5 // Echo Pin
#define trigPin 9 // Trigger Pin
#define LEDPin 13 // Onboard LED
#define audioPin 3
int maximumRange = 200; // Maximum range needed
int minimumRange = 0; // Minimum range needed
long duration, distance; // Duration used to calculate distance

// notes in the melody:
/*
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};
*/
int melody[] = {
  NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
/*
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};
*/
int noteDurations[] = {
  16
};

void runMelody(long distance) {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 1; thisNote++) {

    // to calculate the note duration, take one second divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    //tone(audioPin, melody[thisNote], noteDuration);
    tone(audioPin, distance, noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
  }

}

void setup() {
    pinMode(RXLED, OUTPUT); // Set RX LED as an output
  pinMode(TXLED, OUTPUT); // Set TX LED as an output



 Serial.begin (9600);
 //runMelody();
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);
 //pinMode(LEDPin, OUTPUT); // Use LED indicator (if required)
}

void loop() {
    digitalWrite(RXLED, HIGH); // set the LED off
  digitalWrite(TXLED, LOW); // set the LED off
  delay(300);                       // wait for a second
  digitalWrite(RXLED, LOW); // set the LED on
  digitalWrite(TXLED, HIGH); // set the LED on
  delay(300);  
/* The following trigPin/echoPin cycle is used to determine the
 distance of the nearest object by bouncing soundwaves off of it. */ 
 digitalWrite(trigPin, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH); 
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance = duration/58.2;
 
 if (distance >= maximumRange || distance <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 Serial.println("-1");
 //digitalWrite(LEDPin, HIGH); 
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 Serial.println(distance*1.5 + 120); // cm
 digitalWrite(LEDPin, LOW); 
 runMelody(distance*2 + 250);
 }
 
 //Delay 50ms before next reading.
 delay(50);
}