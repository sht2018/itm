from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc=Minecraft.create()      
pos=mc.player.getTilePos()
mc.player.setTilePos(-30,-6,-40)


ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1] or "UART" in p[1]:
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
#mc.setBlock(pos.x,pos.y,pos.z,block.STONE.id)
x = pos.x
y = pos.y
z = pos.z
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("your position")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if -35<=pos.x<=-25 and -11<=pos.y<=-1 and -45<=pos.z<=-35:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        ser.write("1".encode())
        print("1 send")
        time.sleep(5)
    else:
        stayed_time=0
        
 
