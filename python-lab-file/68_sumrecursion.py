# Program 68 : find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = int(input("Enter the number to find sum upto :"))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))