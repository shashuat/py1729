# Program 26 : Write a program to print the following pattern

'''

*
**
***
**
*

'''

lines= int(input("Enter number of lines to be there in the patterns: "))

for i in range (0, (lines//2) +1, 1):
    for j in range (0, i+1, 1):
        print("*", end ="")
    print()   
    
for i in range (lines//2,0,-1):
    for j in range (0,i,1):
        print("*", end="")
    print()    
