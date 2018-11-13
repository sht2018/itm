# Adventure 3: buildHouse.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a single house, with a doorway, windows,
# a roof, and a carpet.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to Minecraft
mc = minecraft.Minecraft.create()
#mc.player.setTilePos(-30,10,-40)
# A constant, that sets the size of your house
def bu(SIZE):
    # Get the players position
    pos = mc.player.getTilePos()

    # Decide where to start building the house, slightly away from player
    x = pos.x - SIZE/2
    y = pos.y 
    z = pos.z - SIZE/2

    # Calculate the midpoints of the front face of the house
    midx = x+SIZE/2
    midy = y+SIZE/2

    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, 85)

    # Carve the insides out with AIR
    mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)

    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, 50)

    # Carve out the left hand window
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)

    # Carve out the right hand window
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # Add a wooden roof   
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)

    #Add lamps
    mc.setBlocks(x, y+SIZE+1, z, x+SIZE, y+SIZE+1, z+SIZE, 50)
    mc.setBlocks(x, y+SIZE, z-1, x+SIZE, y+SIZE, z-1,50)

    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)

    # END
bu(22)
bu(14)
bu(6)

