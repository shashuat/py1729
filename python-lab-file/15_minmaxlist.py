# Program 15: Given a list of numbers, find maximum and minimum in this list.


a=input('enter the integers').split(" ")
b=[int(i) for i in a]
c=max(b)
d=min(b)
print(c,d)
