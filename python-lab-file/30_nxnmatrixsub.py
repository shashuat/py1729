# Program 30 : Create an n x n square matrix, where all the sub-matrix have the sum of opposite corner elements as even

import itertools

def sub_mat_even(n):
	
	temp = itertools.count(1)
	
	# create a 2d array ranging from 1 to n^2
	l = [[next(temp)for i in range(n)]for i in range(n)]
	
	# If found even we reverse the alternate row elements to get all diagnol elements as all even or all odd
	if n%2 == 0:
		for i in range(0,len(l)):
			if i%2 == 1:
				l[i][:] = l[i][::-1]
	
	# Printing the array formed
	for i in range(n):
		for j in range(n):
			print(l[i][j],end=" ")
		print()

n = 4
sub_mat_even(n)
