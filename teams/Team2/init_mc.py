from mcpi.minecraft import Minecraft
import mcpi.block as block
import argparse

mc=Minecraft.create()

def init(blockID):
    for i in range(-2, 123):
        for j in range(-2, 123):
            for k in range(119,145):
                mc.setBlock(i, k, j, blockID)

    for i in range(-2, 123):
        for j in range(-2, 123):
            for k in range(119,145):
                mc.setBlock(-i, k, j, blockID)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", type=int, help="ID of the block")
    args = parser.parse_args()
    init(args.ID)
