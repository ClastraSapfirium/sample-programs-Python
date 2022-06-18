from glob import glob


x = 0
y = 0

def int(a,b):
    global x
    global y
    x = a
    y = b

def sum ():
    return x + y