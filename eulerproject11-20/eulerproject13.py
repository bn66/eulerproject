"""
Euler Project Problem #13
Large sum
http://projecteuler.net/problem=13
"""

def large_sum(file, number):
    """This function takes the file, puts all numbers in a list, and
    then sums them. It will return the first 'number' digits of the sum
    O(n)
    """
    
    # Open files, splitlines, put into list, and sum.
    numbers = open(file).read()
    numbers = numbers.splitlines()
    numbers = [int(i) for i in numbers]
    
    # Answers
    total = sum(numbers)
    total = str(total)
    digits = total[0:number]
    
    print """The sum of all numbers in %s is %s. The first %d digits are
    %s.
    """ % (file, total, number, digits)


# Tests
# largest_product_series('eulerproject8.txt', 4)

large_sum('eulerproject13.txt', 10)