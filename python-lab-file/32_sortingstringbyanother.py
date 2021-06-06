# Program 32 : Sort a string and return its reverse string according to pattern string

def sortbyPattern(pat, str):

	priority = list(pat)

	# Create a dictionary to store priority of each character
	myDict = { priority[i] : i for i in range(len(priority))}

	str = list(str)

	# Pass lambda function as key in sort function
	str.sort( key = lambda ele : myDict[ele])

	# Reverse the string using reverse()
	str.reverse()

	new_str = ''.join(str)
	return new_str


if __name__=='__main__':
	pat = input()
	str = input()
    
	new_str = sortbyPattern(pat, str)
	print(new_str)
