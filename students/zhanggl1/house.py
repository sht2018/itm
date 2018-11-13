import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
for i in range(30):
    for k in range(30):
        for j in range(30):
            mc.setBlock(pos.x+1+i,pos.y+j,pos.z,0)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+1+i,pos.y+j,pos.z,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+1,pos.y+j,pos.z+i,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+1+i,pos.y+j,pos.z+10,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+11,pos.y+j,pos.z+i,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+1+i,pos.y,pos.z+j,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+1+i,pos.y+10,pos.z+j,17)
for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x+4+i,pos.y+4+j,pos.z,20)
for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x+1,pos.y+4+j,pos.z+4+i,20)
for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x+4+i,pos.y+4+j,pos.z+10,20)
for i in range(3):
    for j in range(3):
        mc.setBlock(pos.x+11,pos.y+4+j,pos.z+4+i,20)
mc.setBlock(pos.x+3,pos.y+2,pos.z,0)
mc.setBlock(pos.x+3,pos.y+1,pos.z,0)
mc.setBlock(pos.x+3,pos.y+1,pos.z+5,62)



