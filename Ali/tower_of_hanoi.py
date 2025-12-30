def hanoi(source, destination, num_disks, pegs):
    if num_disks == 0:
        return
    
    # helper = 'B'
    helper = [peg for peg in pegs if peg not in (source, destination)][0]
    
    hanoi(source, helper, num_disks - 1, pegs)
    
    print(f'Move disk {num_disks} from rod {source} to rod {destination}')
    
    hanoi(helper, destination, num_disks - 1, pegs)
    
pegs = ['A', 'B', 'C']
disks = int(input('Enter number of disks: '))
hanoi(pegs[0], pegs[2], disks, pegs)
print('\nProblem was Solved.')