# Program 26 : Find HCF

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

hcf = compute_hcf(num1, num2)
print("The HCF is", hcf)
