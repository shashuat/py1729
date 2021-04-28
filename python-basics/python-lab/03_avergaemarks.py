# Program 3 : Find aerage of list

list_num = []

# input 
n = int(input("Enter number of elements in list: "))
  
for i in range(0, n):
    ele = int(input("Enter elements: "))
    list_num.append(ele)

# intialise sum_list and iterate
sum_list = 0
for x in list_num:
    sum_list = sum_list + x

average = sum_list/n

print("Average of list is:", average)