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
    
    row_list = []
    col_list = []
    for i in range(0, rows):
        numbers[i] = map(int, numbers[i])
        row_list.append(i)
        col_list.append(0)
        
    print row_list, "row"
    print col_list, "col"
    print numbers
    
    highest_sum = 0
    list = []
    
    window = 1
    
    # while col_list[0] != 1
        # for i in row_list:
            # list.append(numbers[i][col_list[i]])
            # insert sum here
    """
        for i in list
            if list[-window:][0] == list[-window:][1]
        
        list = []
        window += 1
    """
    # let's try something new
    # row_index = 1
    # while row_list != col_list:
        # for i in row_list:
            # list.append(numbers[i][col_list[i]])
            # # sum row, logic check
        # # function to increase column list
        # for i in range(1, len(col_list)):
            # if col_list(i) == col_list(i + 1):
                
            
        # col_list = [0, 1, 2, 3]
            
    
        
    
    
    print list
    

def ep18_recur(a, b):
    """fffffff
    Recursively builds something
    O(???)
    """
    
    if a[-1] + 1 == b[0]:
        return path
    if a[-1] == b[0]: # dive deeper
        ep18_recur([b[0],b[1:])
        
        
    
    
# tests
# max_path('test.txt')
ep18_recur([1],[1,1,1,1])