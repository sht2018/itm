from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
# mc=Minecraft.create("192.168.2.207",4711)

while True:
    hits=mc.events.pollBlockHits() 
    for hit in hits:
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
        for x in range(10):    
            for y in range(10):
                mc.setBlock(hit.pos.x + x, hit.pos.y + y, hit.pos.z, 1)
            for z in range(10):
                mc.setBlock(hit.pos.x, hit.pos.y + x, hit.pos.z + z, 1)
            for a in range(10):
                mc.setBlock(hit.pos.x + 9, hit.pos.y + x, hit.pos.z + a, 1)
            for b in range(10):
                mc.setBlock(hit.pos.x + b, hit.pos.y + x, hit.pos.z + 9 , 1)
        print("House built in (%d, %d, %d)." % (hit.pos.x, hit.pos.y, hit.pos.z))



        
     
