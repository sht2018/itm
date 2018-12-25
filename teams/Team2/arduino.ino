int BuzzerPin=4;
int RedLed =2;
int BlueLed =3;
int Button =5;
int val;

int tone_list[] = {262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1046, 1175, 1318, 1397, 1568, 1760, 1967};
int music_1[] = {12, 10, 12, 10, 12, 10, 9, 10, 12, 12, 12, 10, 13, 12, 10, 12, 10, 9, 8, 9, 10, 12, 10, 9, 8, 9, 10, 0};
float rhythm_1[] = {1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.5, 1, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 2};
int music_2[] = {8, 9, 10, 8, 8, 9, 10, 8, 10, 11, 12, 10, 11, 12, 0};
float rhythm_2[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2};
int music_3[] = {5, 8, 8, 10, 13, 10, 12, 12, 13, 12, 10, 11, 10, 9, 6, 9, 9, 11, 14, 14, 13, 12, 11, 11, 10, 6, 7, 8, 9, 0};
float rhythm_3[] = {0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 1, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 1, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 1, 0.5, 0.25, 0.5, 1, 0.5, 3};
int music_4[] = {5,5,6,5,8,7,5,5,6,5,9,8,5,5,12,10,8,7,6,11,11,10,8,9,8,0};
float rhythm_4[] = {0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,2,0.5,0.5,1,1,1,1,1,0.5,0.5,1,1,1,3};
int music_5[] = {12, 13, 12, 13, 12, 13, 12, 12, 15, 14, 13, 12, 13, 12, 12, 12, 10, 10, 12, 12, 10, 9, 11, 10, 9, 8, 9, 8, 0};
float rhythm_5[] = {0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1};
int music_6[] = {8, 8, 10, 8, 8, 10, 22, 13, 13, 13, 12, 13, 12, 8, 10, 22, 15, 13, 13, 12, 13, 12, 8, 9, 22, 14, 14, 12, 10, 12, 0};
float rhythm_6[] = {1, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 4};
int music_7[] = {6, 8, 9, 10, 12, 10, 8, 9, 6, 22, 8, 9, 10, 12, 12, 13, 9, 10, 22, 10, 12, 13, 12, 13, 15, 14, 13, 12, 13, 10, 8, 9, 10, 12, 8, 6, 8, 9, 10, 13, 12, 0};
float rhythm_7[] = {0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 2, 1, 0.5, 0.5, 0.25, 0.25, 0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.5, 3};
int music_8[] = {10, 8, 9, 6, 10, 9, 8, 9, 6, 10, 8, 9, 9, 12, 10, 7, 8, 8, 7, 6, 7, 8, 9, 5, 13, 12, 10, 10, 9, 8, 9, 10, 9, 10, 9, 12, 12, 12, 12, 12, 12, 0};
float rhythm_8[] = {1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 0.5, 0.5, 1, 0.5, 0.5, 1, 1, 0.5, 0.5, 1, 1, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1};
int music_9[] = {10,12,15,13,12,10,12,13,15,12,15,17,16,15,16,15,13,15,12,0};
float rhythm_9[] = {0.5,0.5,0.5,0.5,2,0.5,0.5,0.5,0.5,2,1,0.5,1,1,0.5,0.5,0.5,0.5,2};
int music_10[] = {10,10,10,8,5,5,22,10,10,10,8,10,22,12,12,10,8,5,5,5,6,7,8,10,9,0};
float rhythm_10[] = {0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,1,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,1};


#define NTDL1 147
#define NTDL2 165
#define NTDL3 175
#define NTDL4 196
#define NTDL5 221
#define NTDL6 248
#define NTDL7 278
#define NTD0 278
#define NTD1 589
#define NTD2 661
#define NTD3 700
#define NTD4 786
#define NTD5 882
#define NTD6 990
#define NTD7 1112
//列出全部D调的频率
#define WHOLE 1
#define HALF 0.5
#define QUARTER 0.25
#define EIGHTH 0.25
#define SIXTEENTH 0.625
//列出所有节拍
int tune[]=                 //根据简谱列出各频率
{
  NTD3,NTD3,NTD4,NTD5,
  NTD5,NTD4,NTD3,NTD2,
  NTD1,NTD1,NTD2,NTD3,
  NTD3,NTD2,NTD2,
  NTD3,NTD3,NTD4,NTD5,
  NTD5,NTD4,NTD3,NTD2,
  NTD1,NTD1,NTD2,NTD3,
  NTD2,NTD1,NTD1,
  
};
float durt[]=                   //根据简谱列出各节拍
{
  1,1,1,1,
  1,1,1,1,
  1,1,1,1,
  1+0.5,0.5,1+1,
  1,1,1,1,
  1,1,1,1,
  1,1,1,1,
  1+0.5,0.5,1+1,
};
int length;
void setup()
{
  Serial.begin(9600);
  pinMode(BuzzerPin,OUTPUT);
  pinMode(RedLed,OUTPUT);
  pinMode(BlueLed,OUTPUT);
  pinMode(Button,INPUT);
  length=sizeof(tune)/sizeof(tune[0]); 
}

void loop()
{
  
  if (Serial.available() > 0) {
    switch (String(Serial.readString()).toInt()) {
     case 1://begin
      for(int x=0;x<length;x++){
        tone(BuzzerPin,tune[x]);
        delay(500*durt[x]);   //这里用来根据节拍调节延时，500这个指数可以自己调整，在该音乐中，我发现用500比较合适。
        noTone(BuzzerPin);
        }
      delay(2000);
      noTone(BuzzerPin);
      break;
     case 2://音乐2,小船
      tone(BuzzerPin,1484);
      delay(5000);
      noTone(BuzzerPin);
      break;
     case 3://音乐3，中型船
      tone(BuzzerPin,742);
      delay(5000);
      noTone(BuzzerPin);
      break;
     case 4://音乐4，大型船
      tone(BuzzerPin,698);
      delay(5000);
      noTone(BuzzerPin);
      break;
     case 5://葫芦娃5
      for (int a = 0; music_6[a] != 0; a++) {
        if (music_6[a] != 22) {
          tone(BuzzerPin, tone_list[music_6[a] - 1]);
        }
        else {
          noTone(BuzzerPin);
         }
        delay(rhythm_6[a] * 300);
        noTone(BuzzerPin);
        delay(30);
      }
        noTone(BuzzerPin);
     case 6://红灯亮
      digitalWrite(RedLed,HIGH);
      break;
     case 7://蓝灯亮
      digitalWrite(BlueLed,HIGH);
      break;
     case 8://红灯灭
      digitalWrite(RedLed,LOW);
      break;
     case 9://蓝灯灭
      digitalWrite(BlueLed,LOW);
      delay(30);
      digitalWrite(RedLed,HIGH);
      delay(30);
      break;
     case 10://机器猫
     for (int a = 0; music_3[a] != 0; a++) {
    if (music_3[a] != 22) {
      tone(BuzzerPin, tone_list[music_3[a] - 1]);
    }
    else {
      noTone(BuzzerPin);
    }
    delay(rhythm_3[a] * 300);
    noTone(BuzzerPin);
    delay(30);
  }
    }
  }
  val=digitalRead(Button);
  if(val==LOW){
    delay(500);
    digitalWrite(BlueLed,HIGH);
    digitalWrite(RedLed,LOW);
    Serial.println("ready");
    delay(500);
    
    }
   else{
    Serial.println("0");
    delay(1000);
    }
   

}
