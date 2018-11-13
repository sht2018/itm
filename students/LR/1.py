import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

for i in range(10):
	for j in range (10):
		mc.setBlock(pos.x+i,pos.y+j,pos.z,17,2)
		mc.setBlock(pos.x,pos.y+j,pos.z+i,17,2)
		mc.setBlock(pos.x+i,pos.y,pos.z+j,17,2)
		mc.setBlock(pos.x+i,pos.y+j,pos.z+9,17,2)
		mc.setBlock(pos.x+9,pos.y+j,pos.z+i,17,2)
		if i<9 and j <9:
			mc.setBlock(pos.x+i,pos.y+9,pos.z+j,block.GLASS.id)
			mc.setBlock(pos.x+i,pos.y+1,pos.z+j,35)
for i in range(16):
	mc.setBlock(pos.x-3,pos.y,pos.z+i-3,139,0)
	mc.setBlock(pos.x+13,pos.y,pos.z+i-3,139,0)
	mc.setBlock(pos.x-3+i,pos.y,pos.z-3,139,0)
	mc.setBlock(pos.x-3+i,pos.y,pos.z+13,139,0)
mc.setBlock(pos.x,pos.y+2,pos.z+2,block.AIR.id)
mc.setBlock(pos.x,pos.y+3,pos.z+2,block.AIR.id)
mc.setBlock(pos.x-1,pos.y+1,pos.z+2,156)
mc.setBlock(pos.x-2,pos.y,pos.z+2,156)
mc.setBlock(pos.x-1,pos.y,pos.z+2,156)

