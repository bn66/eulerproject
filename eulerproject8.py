"""
Euler Project Problem #8
Largest product in a series
http://projecteuler.net/problem=8
"""

import eulerproject3

def largest_product_series(series, consecutive):
    """This function will take in a txt file 'series' with numbers
    and look for the a chain of numbers 'consecutive' long with the
    largest product.
    O(n)
    """
    # Read series, remove \n new lines, initialize variables and lists
    numbers = open(series).read()
    numbers = numbers.replace("\n", "")
    new_numbers = []
    for i in numbers:
        new_numbers.append(int(i))
    answer = 0
    
    # Iteration
    for i in range(0, len(new_numbers) - consecutive):
        products_list =  list(new_numbers[i:i + consecutive])
        if 0 in products_list:  # Skip if zero
            continue
        product = eulerproject3.product(products_list)
        if answer < product:  # Largest product
            answer = product
            
    print """The largest series of %d consecutive numbers in %s is
        %d.""" % (consecutive, series, answer)


# Tests
largest_product_series('eulerproject8.txt', 4)
