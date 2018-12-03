int inpin=7;//定义数字7 接口
int val;//定义变量val
void setup()
{
pinMode(inpin,INPUT);//定义按键接口为输入接口
Serial.begin(9600);
}
void loop()
{
val=digitalRead(inpin);//读取数字7 口电平值赋给val
if(val==LOW)//检测按键是否按下，按键按下时小灯亮起
{ Serial.println("0");}
else
{ Serial.println("1");}
delay(500);
}

