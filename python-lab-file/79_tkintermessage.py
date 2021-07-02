# Program 79 : Make a Tkinter message

from tkinter import *
main = Tk()
ourMessage ='Hello sir! this is shashwat sharma!'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
main.mainloop( )
