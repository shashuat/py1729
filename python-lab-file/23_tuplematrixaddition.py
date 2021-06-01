# Program 23 : demonstrate working of Row-wise element Addition in Tuple Matrix

# initializing list
test_list = [[('smvdu', 5), ('is', 2)], [('best', 4)], [('for', 3), ('me', 2)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Custom eles
cus_eles = [1, 4, 8]

# Row-wise element Addition in Tuple Matrix
# Using enumerate() + list comprehension
res = [[sub + (cus_eles[idx], ) for sub in val] for idx, val in enumerate(test_list)]

# printing result
print("The matrix after row elements addition : " + str(res))
