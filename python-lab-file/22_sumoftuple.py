# Program 22 : demonstrate working of Tuple summation

# initializing tup
test_tup = (1,9,11,15,13,16)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using list() + sum()
res = sum(list(test_tup))

# printing result
print("The summation of tuple elements are : " + str(res))
