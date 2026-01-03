import main

def enqueue(item):
    
    if main.T1 == main.Max - 1 :
        return -1
    
    main.T1+=1
    main.stack_in[main.T1] = item
    