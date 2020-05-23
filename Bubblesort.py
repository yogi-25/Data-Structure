arraytoSort = [16, 19, 11, 15, 10, 12, 14]
#repeating the loop for len(arraytoSort)(number of elements) times
for j in range(len(arraytoSort)):
    #initially swapFlag is returned as false
    swapFlag = False
    i = 0
    while i<len(arraytoSort)-1:
        #compare the adjacent elements
        if arraytoSort[i]>arraytoSort[i+1]:
            #swapping
            arraytoSort[i],arraytoSort[i+1] = arraytoSort[i+1],arraytoSort[i]
            #Changing the value of the swapped elements
            swapFlag = True
        i = i+1
    #if swapFlag is returned as false then the entire list is sorted
    # the loop can be stopped
    if swapFlag == False:
        break
print (arraytoSort)
