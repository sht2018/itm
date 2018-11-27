from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

def run():
    action = "8"
    ser.write(action.encode())
    time.sleep(2)
print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)


mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

mc.player.setTilePos(-30,-6,-40)
flag=False

        

switch=""
while True:
    pos=mc.player.getTilePos()
    resp=ser.readline()
    rs=str(resp)
    if 'ON'in rs:
        print("got ON")
        switch="ON"
        flag=True
    if 'OFF' in rs:
        print("got OFF")
        switch="OFF"
        flag=False
    if flag:
        mc.setBlock(pos.x,pos.y-1,pos.z,20) 

