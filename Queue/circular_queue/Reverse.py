import main

def ReverseQueue():
    global Queue
    global front
    global rear
    global size
    global Max
    
    temp = [0] * main.Max
    index = main.front
    
    for i in range (0 , main.size):
        temp[i] = main.Queue[index]
        index = (index + 1) % main.Max
        
    for i in range (0 , main.size):
        main.Queue[i] = temp[main.size - 1 - i]
    
    
    main.front = 0 
    main.rear = main.size -1
    return main.Queue