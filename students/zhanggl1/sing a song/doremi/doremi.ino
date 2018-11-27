#define BuzzerPin6 13
float tonelist[7]={1046.5,1174.7,1318.5,1396.9,1568,1760,1975.5};

long musiclist[32]={1,2,3,1,1,2,3,1,3,4,5,3,4,5,5,6,5,4,3,1,5,6,5,4,3,1,2,5,1,2,5,1};

long highlist[32]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0};

long rhythmlist[32]={4,4,4,4,4,4,4,4,4,4,2,4,4,2,8,8,8,8,4,4,8,8,8,8,4,4,4,4,2,4,4,2};

void playmusic() {
  for (int i = 1; i <= 32; i = i + (1)) {
    tone(13,tonelist[(int)(musiclist[(int)(i - 1)] - 1)] * pow(2, highlist[(int)(i - 1)]));
    delay((2000 / rhythmlist[(int)(i - 1)]));
    noTone(13);
    delay(10);
  }
}
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
      tone(BuzzerPin6,671);
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
      playmusic();
    }
    delay(500);
    noTone(BuzzerPin6);

  }

}