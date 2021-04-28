# Program 2.1 : Find largest number

list_num = []

# input 
n = int(input("Enter number of elements in list: "))
  
for i in range(0, n):
    ele = int(input("Enter elements: "))
    list_num.append(ele)

# intialise max_num and iterate
max_num = list_num[0]
for x in list_num:
    if x > max_num :
         max_num = x

print("Largest element is:", max_num)
