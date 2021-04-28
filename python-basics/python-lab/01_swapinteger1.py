# Program 1.1: Swap two variables using temp variable

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('after swapping')
print("x =", x)
print("y =", y)