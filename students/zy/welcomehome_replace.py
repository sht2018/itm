from mcpi.minecraft import Minecraft
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
import serial
import serial.tools.list_ports
import time

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)

for p in ports:
    print(p[1])
    if "Arduino" in p[1] or "USB 串行设备" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print("No Arduino Device was found connected to the computer")

mc=Minecraft.create()
while True:
    pos=mc.player.getTilePos()
    mc.postToChat('pos(' + str(pos.x)+ '   ' + str(pos.y) + '   ' + str(pos.z) + ')')
    s = ser.read().decode()
    if s == '1':
        mc.setBlock(pos.x, pos.y -1, pos.z, 20)
