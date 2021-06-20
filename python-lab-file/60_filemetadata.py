# Program 60 : Find metadata of file creation

import os.path, time

file = pathlib.Path('shashwat.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))