# Program 2: Swap two variables with addition/substraction

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

x = x + y
y = x - y
x = x - y

print('after swapping')
print("x =", x)
print("y =", y)