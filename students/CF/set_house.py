import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
texture=79
def set_light(width,height):
        for num in range(width):
                mc.setBlock(pos.x,pos.y,pos.z,)
for height in range(10):
        for a in range(10):
                mc.setBlock(pos.x+a,pos.y+height,pos.z,texture)
                mc.setBlock(pos.x+a,pos.y+height,pos.z+9,texture)
        for b in range(8):
                mc.setBlock(pos.x,pos.y+height,pos.z+b+1,texture)
                mc.setBlock(pos.x+9,pos.y+height,pos.z+b+1,texture)
for floor in range(8):
        for lo in range(8):
                mc.setBlock(pos.x+floor+1,pos.y,pos.z+1+lo,texture)
for roof in range(8):
        for lon in range(8):
                mc.setBlock(pos.x+roof+1,pos.y+9,pos.z+1+lon,texture)
for secondfloor in range(8):
        for lo in range(8):
                mc.setBlock(pos.x+secondfloor+1,pos.y+4,pos.z+1+lo,texture)
mc.setBlock(pos.x+4,pos.y+1,pos.z,0)
mc.setBlock(pos.x+4,pos.y+2,pos.z,0)
mc.setBlock(pos.x+5,pos.y+1,pos.z,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z,0)
for ii in range(3):
        for iii in range(2):
                mc.setBlock(pos.x+1+ii,pos.y+4,pos.z+1+iii,0)

for hei in range(3):
        mc.setBlock(pos.x+1+hei,pos.y+3-hei,pos.z+1,53)
        mc.setBlock(pos.x+1+hei,pos.y+3-hei,pos.z+2,53)

        
        




                
                
