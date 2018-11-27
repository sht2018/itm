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

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

pos = mc.player.getTilePos()

def run():
    action = "empty"
    while True:
        hits=mc.events.pollBlockHits() 
        for hit in hits:
            mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
            action = str(abs(pos.x-hit.pos.x) % 21)
            ser.write(action.encode())
            time.sleep(0.5)

run()