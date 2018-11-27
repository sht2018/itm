int val;//定义变量val
int ledpin=13;//定义数字接口13
void setup()
{
  Serial.begin(9600);//设置波特率为9600，这里要跟软件设置相一致。当接入特定设备（如：蓝牙）时，我们也要跟其他设备的波特率达到一致。
  pinMode(ledpin,OUTPUT);//设置数字13 口为输出接口，Arduino 上我们用到的I/O 口都要进行类似这样的定义。
}
void loop()
{
  val=Serial.read();//读取PC 机发送给Arduino 的指令或字符，并将该指令或字符赋给val
  if(val=='y')//判断接收到的指令或字符是否是“R”。
  {  //如果接收到的是“R”字符
    float tonelist[7]={1046.5,1174.7,1318.5,1396.9,1568,1760,1975.5};

    long musiclist[32]={1,2,3,1,1,2,3,1,3,4,5,3,4,5};

    long highlist[32]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0};

    long rhythmlist[32]={4,4,4,4,4,4,4,4,4,4,2,4,4,2,8,8,8,8,4,4,8,8,8,8,4,4,4,4,2,4,4,2};
    for (int i = 1; i <= 14; i = i + (1)) {
      tone(10,tonelist[(int)(musiclist[(int)(i - 1)] - 1)] * pow(2, highlist[(int)(i - 1)]));
      delay((2000 / rhythmlist[(int)(i - 1)]));
      noTone(10);
      delay(10);
    }
    Serial.println("Hello World!");//显示“Hello World！”字符串
  }
}

