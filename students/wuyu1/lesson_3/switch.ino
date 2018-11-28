int inpin=2;
int val;//定义变量val
void setup()
{
  pinMode(inpin,INPUT);//定义按键接口为输入接口
  Serial.begin(9600);
}
void loop(){
  val=digitalRead(inpin);//读取数字7 口电平值赋给val
  if(val==0){ 
    Serial.println("OFF");
   }
  else if(val==1){
    Serial.println("ON");
   }
}
