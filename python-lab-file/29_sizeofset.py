# Program 29 : Find out size of set

import sys

# sample Sets
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Person1", "Raju", "Person2", "Nikhil", "Person3", "Shashwat"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

# print the sizes of sample Sets
print("Size of Set1: " + str(sys.getsizeof(Set1)) + "bytes")
print("Size of Set2: " + str(sys.getsizeof(Set2)) + "bytes")
print("Size of Set3: " + str(sys.getsizeof(Set3)) + "bytes")
