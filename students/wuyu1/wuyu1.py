from mcpi.minecraft import Minecraft
import time


#不断检查宝剑右键敲击方块的事件并打印出来，如果在家附近敲击，可以立即飞起

mc=Minecraft.create()
#mc=Minecraft.create("192.168.2.207",4711)

stayed_time=0

while True:
    
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    
    pos=mc.player.getTilePos()

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


        
     
