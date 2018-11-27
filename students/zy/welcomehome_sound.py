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
 time.sleep(2)
 def run(num):
    action = str(num)
    ser.write(action.encode())
    time.sleep(1)
 mc=Minecraft.create()
 stayed_time=0
def clean():
    pos=mc.player.getTilePos()
    for i in range(-50,51):
        for j in range(-50,51):
            for k in range(-50,51):
                mc.setBlock(pos.x + i, pos.y + j ,pos.z + k, 0)
                time.sleep(0.1)
'''
while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.player.setTilePos(-30,30,-60)
    if pos.x == -30 and pos.y == 40 and pos.z == -60:
        break
'''
while True:
    time.sleep(0.4)
    pos=mc.player.getTilePos()
    mc.postToChat('pos(' + str(pos.x)+ '   ' + str(pos.y) + '   ' + str(pos.z) + ')')
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    if pos.x == -30 and pos.y == -6 and pos.z == -40:
        run(1)
    else:
        run(0)