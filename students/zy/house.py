from mcpi.minecraft import Minecraft
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
#    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.player.setTilePos(-4000,80,-5000)
    if pos.x == -4000 and pos.y == 80 and pos.z == -5000:
        break
for i in range(0,10):
    for j in range(0,10):
        mc.setBlock(pos.x + 30 + i, pos.y - 20, pos.z + j, 5)
        for k in range(1,10):
            if i == 0 or i == 9:
                mc.setBlock(pos.x + 30 + i, pos.y + k - 20, pos.z + j, 5)
            if j == 0 or j == 9:
                mc.setBlock(pos.x + 30 + i, pos.y + k - 20, pos.z + j, 5)
for i in range(0,10):
    for j in range(0,10):
        mc.setBlock(pos.x + 30 + i, pos.y - 10, pos.z + j, 5)
        mc.setBlock(pos.x + 30 + i, pos.y - 9, pos.z + j, 50)
