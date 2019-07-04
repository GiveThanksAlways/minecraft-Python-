from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle
#from celAutomataRules import applyRule, printLine, printStart
import celAutomataRules

mc = Minecraft.create()
pos = mc.player.getPos()

terrapin = MinecraftTurtle(mc, pos)



terrapin.fly()
terrapin.speed(0)
#terrapin.penblock(3)

arr = []
celAutomataRules.fillWithZeros(arr,30)
arr.append(1)
celAutomataRules.fillWithZeros(arr,30)

update_arr = []

celAutomataRules.fillWithZeros(update_arr,len(arr))



for i in range(len(arr)):
    celAutomataRules.printLine(arr, terrapin)
    terrapin.setz(pos.z+1)# next line 

    celAutomataRules.arr1ToArr2(arr,update_arr)
    arr = list(update_arr)
    
    
        
    









    
    
            
   
                                
