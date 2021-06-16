# Program 45 : Implementation of Insertion Sort

def insertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]

		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key

arr = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele)

insertionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

