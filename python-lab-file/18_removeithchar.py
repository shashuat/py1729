# Program 18 : method to remove i'th character

# Initializing String
test_str = input()

# Printing original string
print ("The original string is : " + test_str)

# Removing char at pos 3
# using loop
new_str = ""

for i in range(len(test_str)):
	if i != 2:
		new_str = new_str + test_str[i]

# Printing string after removal
print ("The string after removal of i'th character : " + new_str)
