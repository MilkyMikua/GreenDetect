// test serial number
#include <Servo.h>
Servo myservo;

int pos = 0; 
int x;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  myservo.attach(A0);  // attaches the servo on pin A0 to the servo object

}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();

  if (x == 1) {
  myservo.write(180);
  delay(1500);
}
  
  else if(x == 0){
    myservo.write(100);
    delay(1500);
  }

}

/*
void green() {
  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  exit(0);
}

void nogreen() {
for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }                       // waits 15ms for the servo to reach the position
  }
  */