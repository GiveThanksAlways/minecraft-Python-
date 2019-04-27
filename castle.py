from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# Post to chat
mc.postToChat("Hello World")


# place a block code
x, y, z = mc.player.getPos()
#blockType = 15 
#mc.setBlock(x+1, y, z, blockType)

x = x + 5
y = y + 5
blockTypeA = 15
for i in range(8):
	for j in range(8):
		for k in range(8):
			mc.setBlock(x+i, y+j, z+k, blockTypeA)
