class Array:
    def __init__(self, array_size):
        self.array = [None] * array_size
        self.arr_size = array_size
        
    def insert(self, value, index):
        if index < self.arr_size:
            self.array[index] = value
        else:
            print('Please enter valid index...')
    
    def show(self):
        print(self.array)

# Test...

arr = Array(4)
arr.insert('hello', 3)
arr.show()