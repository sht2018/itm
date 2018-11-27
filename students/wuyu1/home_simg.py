from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "COM" in p[1] or "USB 串行设备" in p[1]:
        ser=serial.Serial(port=p[0])
    else :
        print ("No Arduino Device was found connected to the computer")

time.sleep(2)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x>=-40 and pos.x<=20 and pos.y<=4 and pos.y>=-16 and pos.z<=-30 and pos.z>=-50:
        mc.postToChat("welcome home")
        ser.write(str(1).encode())
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     