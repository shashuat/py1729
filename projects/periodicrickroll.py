import time
import webbrowser

total_breaks=10
break_count=0

print("This Program Started on " + time.ctime())

while(break_count < total_breaks):
    time.sleep(69)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count=break_count+1
