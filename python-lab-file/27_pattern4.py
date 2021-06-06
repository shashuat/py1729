# Program 27:Write a program to print the following pattern

'''

__*
_***
*****

'''


lines= int(input("Enter number of lines to be there in the patterns: "))
print()    
print("******Pattern 1*******")
print()
for i in range (0, lines, 1):
    for j in range (lines-1,i,-1):
        print("_", end="")     
    
    for k in range (0, 2*i +1, 1):
        print ("*", end="")
    
    print()    

