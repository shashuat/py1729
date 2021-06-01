# Program 16 : to swap first and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [10,20,30,13,25,67]

print(swapList(newList))
