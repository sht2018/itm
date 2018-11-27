import serial
import time
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
player = mc.player

ser=serial.Serial(port='COM3')
time.sleep(2)

while True:
    resp=ser.readline()
    rs=str(resp)
    pos = player.getTilePos()
    if '0' in rs:
        print("Turn off glass")
    if '1' in rs:
        print("Turn on glass")
        mc.setBlock(pos.x, pos.y - 1, pos.z, 20)