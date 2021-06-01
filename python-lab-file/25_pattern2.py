# Program 25 :Write a program to print the Diamond Pattern
'''

         *
      *    *
  *     *     *
     *      *
         *
         
'''

lines= int(input("Enter number of lines to be there in the patterns: "))
midPoint= lines//2  # Note: integer division

for i in range (0, midPoint+1, 1):
    for j in range (midPoint,i,-1):
        print(" ", end="")         
    for k in range (0, 2*i +1, 1):
        print ("*", end="")    
    print()    
    
for i in range (0, midPoint, 1):
    for j in range (0,i+1,1):
        print(" ", end="")     
    
    for k in range (0, 2*midPoint - 2*i - 1, 1)    :
        print("*", end="")       
    print()   
