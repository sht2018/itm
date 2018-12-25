import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
a,b,c=pos.x,pos.y,pos.z
for j in range(1,9):
    mc.setBlock(pos.x+j, pos.y, pos.z,1)
    pos.x=pos.x+j
    for i in range(1,5):
        mc.setBlock(pos.x, pos.y, pos.z+i,1)
    pos.x=a    
for j in range(1,9):
    mc.setBlock(pos.x+j, pos.y+1, pos.z,89)
    pos.x=pos.x+j
    for i in range(1,5):
        mc.setBlock(pos.x, pos.y+1, pos.z+i,89)
    pos.x=a
for j in range(1,9):
    mc.setBlock(pos.x+j, pos.y+2, pos.z,5)
    pos.x=pos.x+j
    for i in range(1,5):
        mc.setBlock(pos.x, pos.y+2, pos.z+i,5)
    pos.x=a      
for j in range(5,9):
    mc.setBlock(pos.x+j, pos.y+2, pos.z,102)
    pos.x=pos.x+j
    for i in range(1,5):
        mc.setBlock(pos.x, pos.y+2, pos.z+i,102)
    pos.x=a 
for j in range(1,9):
    mc.setBlock(pos.x+j, pos.y+3, pos.z,24,2)
    pos.x=pos.x+j
    for i in range(1,5):
        mc.setBlock(pos.x, pos.y+3, pos.z+i,24,2)
    pos.x=a  
for j in range(2,5):
    mc.setBlock(pos.x+j, pos.y, pos.z+1,126)
    pos.x=pos.x+j
    for i in range(1,3):
        mc.setBlock(pos.x, pos.y, pos.z+i+1,126)
    pos.x=a    
pos.y=b+3
for j in range(2,8):
    mc.setBlock(pos.x+j, pos.y, pos.z+1,126)
    pos.x=pos.x+j
    for i in range(1,3):
        mc.setBlock(pos.x, pos.y, pos.z+i+1,126)
    pos.x=a    
pos.y=b
for j in range(5,8):
    mc.setBlock(pos.x+j, pos.y, pos.z+1,5)
    pos.x=pos.x+j
    for i in range(1,3):
        mc.setBlock(pos.x, pos.y, pos.z+i+1,5)
    pos.x=a    
for j in range(2,8):
    mc.setBlock(pos.x+j, pos.y+2, pos.z+1,0)
    pos.x=pos.x+j
    for i in range(1,3):
        mc.setBlock(pos.x, pos.y+2, pos.z+i+1,0)
    pos.x=a
for j in range(2,8):
    mc.setBlock(pos.x+j, pos.y+1, pos.z+1,0)
    pos.x=pos.x+j
    for i in range(1,3):
        mc.setBlock(pos.x, pos.y+1, pos.z+i+1,0)
    pos.x=a       
 

