const int buttonPin = 2;
const int ledPin =  13;
int buttonState = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  //pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    //digitalWrite(ledPin, HIGH);
    Serial.write("1\n");
  } else {
    //digitalWrite(ledPin, LOW);
    Serial.write("0\n");
  }
  delay(1000);
}