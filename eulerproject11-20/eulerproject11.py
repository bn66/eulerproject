"""
Euler Project Problem #11
Largest product in a grid
http://projecteuler.net/problem=11
"""

import eulerproject3

def largest_product_grid(file, consecutive):
    """This function will take in the 'file' txt file with numbers
    and look for the a series adjacent numbers in a line 'consecutive'
    long with the largest product. The numbers must be rectangular
    Because multiplication is commutative, only four sets of directions
    will have unique results: 
    | - \ /, vertical, horizontal, backslash and forward slash.
    The horizontal search pattern borrows heavily from eulerproject8
    All search algorithms use i for rows and j for columns, searching
    from the left to the right and top to bottom. 'k' compiles a list
    O(n^3)
    """
    # Read file, create iterable 2D list, initialize variables
    numbers = open(file).read()
    numbers = numbers.splitlines()
    numbers = [i.split() for i in numbers]
    
    rows = len(numbers)
    columns = len(numbers[1])
    answer_product = 0
    answer_list = []
    
    product = 1
    multiply_list = []
    
    for i in range(0, rows):
        numbers[i] = map(int, numbers[i])

    # Horizontal, - , similar to eulerproject8.py, build left to right
    for i in range(0, rows):
        for j in range(0, columns - consecutive + 1):
            product = reduce(lambda x, y: x * y,
                numbers[i][j:j + consecutive])
            multiply_list = [numbers[i][j:j + consecutive]]
            if answer_product < product:
                answer_product = product
                answer_list = multiply_list
            multiply_list = []
            product = 1
    
    # Verticals, | , build list top down
    for i in range(0, rows - consecutive + 1):
        for j in range(0, columns):
            for k in range(0, consecutive):
                if numbers[k + i][j] ==  0:
                    break
                product *= numbers[k + i][j]
                multiply_list.append(numbers[k + i][j])
                if answer_product < product:
                    answer_product = product
                    answer_list = multiply_list
            multiply_list = []
            product = 1

    # Forward Diagonal, / , builds from the bottom left to top right
    for i in range(0, rows - consecutive + 1):
        for j in range(0, columns - consecutive + 1):
            for k in range(0, consecutive):
                if numbers[i + (consecutive - k - 1)][j + k] ==  0:
                    break
                product *= numbers[i + (consecutive - k - 1)][j + k]
                multiply_list.append(numbers[i + (consecutive - k - 1)]
                [j + k])
                if answer_product < product:
                    answer_product = product
                    answer_list = multiply_list
            multiply_list = []
            product = 1


    # Backward Diagonal, \ , builds from top left to bottom right
    for i in range(0, rows - consecutive + 1):
        for j in range(0, columns - consecutive + 1):
            for k in range(0, consecutive):
                if numbers[i + k][j + k] ==  0:
                    break
                product *= numbers[i + k][j + k]
                multiply_list.append(numbers[i + k][j + k])
                if answer_product < product:
                    answer_product = product
                    answer_list = multiply_list
            multiply_list = []
            product = 1
                    
    print """The largest product in %s is %d. %d is a product of %r.
            """ % (file, answer_product, answer_product, answer_list)

largest_product_grid('eulerproject11.txt', 4)
# running multiplication, make columns dependent on rows