# Program 61 : Compute the Power of a Number

base = int(input("enter the base"))
exponent = int(input("enter the exponent"))

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))