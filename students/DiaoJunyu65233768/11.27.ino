  #include <String.h>
float tonelist[7]={1046.5,1174.7,1318.5,1396.9,1568,1760,1975.5};

long musiclist[32]={1,2,3,1,1,2,3,1,3,4,5,3,4,5,5,6,5,4,3,1,5,6,5,4,3,1,2,5,1,2,5,1};

long highlist[32]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0};

long rhythmlist[32]={4,4,4,4,4,4,4,4,4,4,2,4,4,2,8,8,8,8,4,4,8,8,8,8,4,4,4,4,2,4,4,2};
const int speakerPin = 11; 
const int buttonPin = 2; 
const int ledPin = 13; 
int buttonState = 0;
int val;
bool flag = false;
int de = 500;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(speakerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin,INPUT_PULLUP);
  Serial.begin(9600);
}

void playmusic() {
  for (int i = 1; i <= 32; i = i + (1)) {
    tone(11,tonelist[(int)(musiclist[(int)(i - 1)] - 1)] * pow(2, highlist[(int)(i - 1)]));
    delay((2000 / rhythmlist[(int)(i - 1)]));
    noTone(10);
    delay(10);
  }
}
void play() {
  tone(speakerPin,tonelist[0]);
  delay(60);
  tone(speakerPin,tonelist[1]);
  delay(60);
  tone(speakerPin,tonelist[2]);
  delay(60);
  noTone(speakerPin);
  delay(10);
}

// the loop function runs over and over again forever
void loop() {
  buttonState = digitalRead(buttonPin);
  //digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Serial.println("OFF");
    if (flag == true) flag = false;
    delay(100);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    //if (flag == false) play();
    flag = true;
    Serial.println("ON");
    delay(100);
  }
  val=Serial.read();//读取PC 机发送给Arduino 的指令或字符，并将该指令或字符赋给val
  if(val=='R')//判断接收到的指令或字符是否是“R”。
  {  //如果接收到的是“R”字符
    play();
  }
}