# Program 2.2 : Find largest number

list_num = []

# input 
n = int(input("Enter number of elements in list: "))
  
for i in range(0, n):
    ele = int(input("Enter elements: "))
    list_num.append(ele)

print("Largest element is:", max(list_num))
