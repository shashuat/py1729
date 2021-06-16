# Program 41 : Implement Linear search

def linear_search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele)
     
x = int(input("Enter element to be searched : "))

result = linear_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")