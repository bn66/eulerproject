"""
Euler Project Problem #18
Maximum Path Sum I
http://projecteuler.net/problem=18
"""

def max_path(file):
    """fffffff
    Borrows from eulerproject11 code
    O(???)
    """
    # Read file, create iterable 2D list, initialize variables
    numbers = open(file).read()
    numbers = numbers.splitlines()
    numbers = [i.split() for i in numbers]
    
    rows = len(numbers)
    # columns = len(numbers[1]) # *************
    
    for i in range(0, rows):
        numbers[i] = map(int, numbers[i])
    
    sum_list = [numbers[i]]]
    
    print numbers
    
    # for each entry in column, each entry in the list
    # top to bottom
    for i in range(0, rows):
        for j in range(0, len(i)):
            
    
  
# tests
max_path('eulerproject18.txt')