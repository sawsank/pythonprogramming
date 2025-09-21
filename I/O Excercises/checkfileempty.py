import os

size = os.stat("I/O Excercises/test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print('file is not empty')