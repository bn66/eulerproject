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
    # best path
    
    while col_list != row_list:
        list = []
        for i in range(0, len(row_list)):
            list.append(numbers[row_list[i]][col_list[i]])
        sum = reduce(lambda x, y: x+y, list)
        # print sum
        if highest_sum < sum:
            highest_sum = sum
        for i in range(1, len(col_list)):
            # print col_list[-i]
            if col_list[-i] == col_list[-i-1]:
                col_list[-i] += 1
                col_list[-i:] = [col_list[-i]] * (i)
                break
            elif col_list[-i] + 1 == col_list[-i-1]:
                continue
        # print col_list
    
    print highest_sum
# tests
max_path('eulerproject18.txt')
# max_path('test.txt')