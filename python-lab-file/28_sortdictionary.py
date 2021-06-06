# Program 28 :  Create a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'santosh':'10','shashwat':'9','arjun':'15','yash':'2','aryan':'32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
