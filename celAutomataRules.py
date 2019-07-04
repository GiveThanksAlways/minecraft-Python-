from mcpi import block

def fillWithZeros(arr, size):
    for i in range(size):
        arr.append(0)

def arr1ToArr2(arr1, arr2):
    for i in range(1,len(arr1)-1): # go from 1 to len -1 because of the i-1 and i+1 parts
        arr2[i] = applyRuleSet(arr1[i-1],arr1[i],arr1[i+1])




# Cellular automaton rule 90     
def applyRule90(left, middle, right):
    filledIn = 1
    empty = 0
    
    if left == 1:
        #rule 1,2,3,4
        if middle == 1:
            if right == 1:
                #rule 1
                return empty
            else:
                #rule 2
                return filledIn
        elif right == 1:
            #rule 3
            return empty
        else:
            #rule 4
            return filledIn

    elif middle == 1:
        #rule 5, 6
        if right == 1:
            #rule 5
            return filledIn
        else:
            #rule 6
            return empty

    elif right == 1:
        #rule 7
        return filledIn
    else:
        #rule 8
        return empty

# Cellular automaton rule set by array   
def applyRuleSet(left, middle, right):
    rule_arr = [0,1,1,1,1,1,0,0]
    
    if left == 1:
        #rule 1,2,3,4
        if middle == 1:
            if right == 1:
                #rule 1
                return rule_arr[0]
            else:
                #rule 2
                return rule_arr[1]
        elif right == 1:
            #rule 3
            return rule_arr[2]
        else:
            #rule 4
            return rule_arr[3]

    elif middle == 1:
        #rule 5, 6
        if right == 1:
            #rule 5
            return rule_arr[4]
        else:
            #rule 6
            return rule_arr[5]

    elif right == 1:
        #rule 7
        return rule_arr[6]
    else:
        #rule 8
        return rule_arr[7]


def printLine( arr, terrapin):
    arr_size = len(arr)
    
    terrapin.pendown()
    for i in range(arr_size):
        # set block type to draw with
        if arr[i] == 1:
            terrapin.penblock(80)#block.GOLD_BLOCK.id
        else:
            terrapin.penblock(79)
    
        terrapin.forward(0) # draw

        # don't move forward if we are on the last arr element
        if i != arr_size -1:
            terrapin.forward(1)
            
    terrapin.penup()
    terrapin.backward(arr_size-1)
    

def rightTurn( arr, terrapin):
    terrapin.right(90)
    terrapin.forward(1)
    terrapin.right(90)

def leftTurn( arr, terrapin):
    terrapin.left(90)
    terrapin.forward(1)
    terrapin.left(90)
    
    







    
    
    
