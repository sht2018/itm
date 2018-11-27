#define BuzzerPin4 4
int tone_list[] = {262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1046, 1175, 1318, 1397, 1568, 1760, 1967};
int music_1[] = {12, 10, 12, 10, 12, 10, 9, 10, 12, 12, 12, 10, 13, 12, 10, 12, 10, 9, 8, 9, 10, 12, 10, 9, 8, 9, 10, 0};
float rhythm_1[] = {1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.5, 1, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 2};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0) {
    String action = String(Serial.readString());
    if (action == "sing"){
      for (int a = 0; music_1[a] != 0; a++) {
        if (music_1[a] != 22) {
          tone(BuzzerPin4, tone_list[music_1[a] - 1]);
        }
        else {
          noTone(BuzzerPin4);
        }
        delay(rhythm_1[a] * 300);
        noTone(BuzzerPin4);
        delay(30);
      };
    };
  };
  delay(1000);
}