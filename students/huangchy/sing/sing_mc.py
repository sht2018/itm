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

pos = mc.player.getTilePos()

action = "empty"
while True:
    
    time.sleep(0.5)
    
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=30 y=0 z=80 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    if pos.x==30 and pos.y==0 and pos.z==80:
        mc.postToChat("welcome home")
        action = "sing"
        ser.write(action.encode())
        time.sleep(5)