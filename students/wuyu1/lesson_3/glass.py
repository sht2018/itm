from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "COM" in p[1] or "UART" in p[1] :
        ser=serial.Serial(port=p[0])
    else :
        print ("No Arduino Device was found connected to the computer")


time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    resp=ser.readline()
    rs=str(resp)
    if 'ON' in rs:
        mc.setBlock(pos.x, pos.y, pos.z, 20)



        
     
