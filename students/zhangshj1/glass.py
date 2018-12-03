from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
	    print ("ok")
    else :
	    print ("No Arduino Device was found connected to the computer")
#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    
    time.sleep(1)
    print(int(ser.readline()))
    if int(ser.readline())==1:
        mc.postToChat("glass palced")
        pos=mc.player.getTilePos()
        mc.setBlock(pos.x,pos.y-1,pos.z,20)
    else:
        print("glass not placed");
