#define BuzzerPin6 6
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0) {
    switch (String(Serial.readString()).toInt()) {
     case 1:
      tone(BuzzerPin6,523);
      break;
     case 2:
      tone(BuzzerPin6,587);
      break;
     case 3:
      tone(BuzzerPin6,659);
      break;
     case 4:
      tone(BuzzerPin6,698);
      break;
     case 5:
      tone(BuzzerPin6,784);
      break;
     case 6:
      tone(BuzzerPin6,880);
      break;
     case 7:
      tone(BuzzerPin6,988);
      break;
     case 8:
      tone(BuzzerPin6,1046);
      break;
    }
    delay(500);
    noTone(BuzzerPin6);

  }

}
