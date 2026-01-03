import main

def find (item):
    i = 0
    for i in range (0 , main.size):
        if main.Array[i] == item:
            return i
        
    return -1