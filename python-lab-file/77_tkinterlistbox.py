# Program 77 : Make tkinter listbox

from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'SMVDU')
Lb.insert(2, 'NIT K')
Lb.insert(3, 'IIT J')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()
