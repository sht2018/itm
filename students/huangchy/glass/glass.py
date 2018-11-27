from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos = mc.player.getTilePos()

import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

time.sleep(2)

while True:
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        print("got ON")
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y-1, pos.z, 20)
    if 'OFF' in rs:
        print("got OFF")
    time.sleep(0.1) 