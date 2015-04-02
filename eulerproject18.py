"""
Euler Project Problem #18
Maximum Path Sum I
http://projecteuler.net/problem=18
"""

def max_path_sum(file):
    """Brute force solution to search for a path from top to bottom in a
    number triangle defined in a txt file. Prints the path of the
    highest sum with its value.
    O(n)
    """
    # Read file, create iterable 2D list "numbers"
    numbers = open(file).read()
    numbers = numbers.splitlines()
    numbers = [i.split() for i in numbers]
    
    # Take 'int' of numbers
    # Create a list of rows and changing column indexes
    rows = len(numbers)
    row_list = []
    col_list = []
    for i in range(0, rows):
        numbers[i] = map(int, numbers[i])
        row_list.append(i)
        col_list.append(0)
        
    # print numbers, "Triangle"
    
    # Answers
    highest_sum = 0
    highest_path = []
    
    # Brute force search from top to bottom, left to right
    while col_list != row_list: # Right side of triangle is last
        list = [] 
        for i in range(0, len(row_list)): # Construct list of numbers
            list.append(numbers[row_list[i]][col_list[i]])
        sum = reduce(lambda x, y: x+y, list)
        
        if highest_sum < sum:
            highest_sum = sum
            best_path = list
            
        # Construct list by changing bottom values and working upwards
        for i in range(1, len(col_list)):
            if col_list[-i] == col_list[-i-1]:
                col_list[-i] += 1
                col_list[-i:] = [col_list[-i]] * (i)
                break
            elif col_list[-i] + 1 == col_list[-i-1]:
                continue
    
    print highest_sum
    print highest_path

# tests
# max_path_sum('eulerproject18.txt')