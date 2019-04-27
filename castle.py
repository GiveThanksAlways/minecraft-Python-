from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# Post to chat
mc.postToChat("Hello World")


# place a block code
x, y, z = mc.player.getPos()
blockType = 15 
mc.setBlock(x+1, y, z, blockType)
