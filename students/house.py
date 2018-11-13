import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+j+1,pos.y+i,pos.z,block.STONE.id)
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+10,pos.y+i,pos.z+j,block.STONE.id)
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+j+1,pos.y+i,pos.z+9,block.STONE.id)
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+1,pos.y+i,pos.z+j,block.STONE.id)
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+j+1,pos.y+9,pos.z+i,block.STONE.id)
for i in range (10):
    for j in range (10):
        mc.setBlock(pos.x+j+1,pos.y-1,pos.z+i,block.STONE.id)

mc.setBlock(pos.x+5,pos.y,pos.z,0)
mc.setBlock(pos.x+5,pos.y+1,pos.z,0)
