from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import time

#请自行修改服务器的ip地址
mc=Minecraft.create()

stayed_time=0

class house:
    def __init__(self,hit,width,length,height):
        for x in range(width):
            for z in range(length):
                mc.setBlock(hit.pos.x + x, hit.pos.y, hit.pos.z + z, 5)
        for y in range(height):
            for x in range(width):
                mc.setBlock(hit.pos.x + x,hit.pos.y + y + 1, hit.pos.z,1)
                mc.setBlock(hit.pos.x + x,hit.pos.y + y + 1, hit.pos.z + 4,1)
            for z in range(length):
                mc.setBlock(hit.pos.x, hit.pos.y + y + 1, hit.pos.z + z,1)
                mc.setBlock(hit.pos.x + 4, hit.pos.y + y + 1, hit.pos.z + z,1)
        for x in range(width):
            for z in range(length):
                mc.setBlock(hit.pos.x + x, height,hit.pos.z + z, 35)
        mc.setBlock(hit.pos.x + width // 2, hit.pos.y + 1, hit.pos.z,0)
        mc.setBlock(hit.pos.x + width // 2, hit.pos.y + 2, hit.pos.z,0)
        mc.setBlock(hit.pos.x + width // 2, height - 1, hit.pos.z + length // 2, 89)




while True:
    print("stay_time"+str(stayed_time))
    stayed_time+=1
    time.sleep(0.5)
    hits=mc.events.pollBlockHits() 
    for hit in hits:
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z)+"f"+str(hit.face)+"     id:"+str(hit.entityId))
        h = house(hit,5,5,5)
