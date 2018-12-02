from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc=Minecraft.create()
pos=mc.player.getTilePos()
#mc.setBlock(pos.x,pos.y,pos.z,block.GLASS.id)
ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "Arduino" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
time.sleep(2)


while True:
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        print("got ON")
        mc.postToChat("got ON")
        mc.setBlock(pos.x,pos.y,pos.z,block.GLASS.id)
    if 'OFF' in rs:
        print("got OFF")    
        
 
