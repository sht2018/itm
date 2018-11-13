from mcpi.minecraft import Minecraft
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)       
pos=mc.player.getTilePos()
#mc.setBlock(pos.x+3,pos.y,pos.z,block.STONE.id)
for a in range(10):
    for b in range(10):
        for c in range(10):
            mc.setBlock(pos.x+c,pos.y+b,pos.z+a,block.STONE.id)
for a in range(8):
    for b in range(8):
        for c in range(8):
            mc.setBlock(pos.x+c+1,pos.y+b+1,pos.z+a+1,block.AIR.id)
for a in range(4):
    for b in range(4):
        mc.setBlock(pos.x+b+3,pos.y+a,pos.z,block.AIR.id)
