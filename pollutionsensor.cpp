int  limit_value = 650; 
// define the value at risk from Gas.
const int buzzer = 6;
void setup() {
  Serial.begin(9600); 
  // Used to activate the serialmotor.
  pinMode(8, OUTPUT); 
  // Pin 8 is activated as an output, to turn on a Green led.
  pinMode(7, OUTPUT); 
  // Pin 7 is activated as an output, to turn on a Red led.
  pinMode(buzzer, OUTPUT); 
  // Buzzer
}

void loop() {
  Serial.println(analogRead(A0)); 
  // A condition is defined. If the sensor reading is higher than the limit_value or not,
  // it will perform an action say x.

  if(analogRead(A0) > limit_value){ 
    // If this condition is met, the following will occur.
    digitalWrite(8, LOW); 
    // The Green LED turns off.
    digitalWrite(7, HIGH); 
    // The Red LED will turn on.
    tone(buzzer, 1200);
    // The buzzer will start buzzing and show a sign of danger.
    delay(500);
  } else{ 
    // IF the first condition is not met, this will happen.
    digitalWrite(8, HIGH); 
    // The Green LED will turn on.
    digitalWrite(7, LOW); 
    // The Red LED turns off.
    noTone(buzzer);
    // The buzzer will stop buzzing.
    delay(500);
  }
  delay (500);
}