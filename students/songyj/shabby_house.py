import mcpi.minecraft as minecraft
import mcpi.block as block
import secrets
mc = minecraft.Minecraft.create()
blocks = [1]

def shabby_house(x, y, z):
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x - 5, y + i, z + j, secrets.choice(blocks))
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x + 5, y + i, z + j, secrets.choice(blocks))
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x + i, y - 5, z + j, secrets.choice(blocks))
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x + i, y + 5, z + j, secrets.choice(blocks))
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x + i, y + j, z - 5, secrets.choice(blocks))
    for i in range(-5, 6):
        for j in range(-5, 6):
            mc.setBlock(x + i, y + j, z + 5, secrets.choice(blocks))

pos = mc.player.getTilePos()
shabby_house(pos.x, pos.y, pos.z)
