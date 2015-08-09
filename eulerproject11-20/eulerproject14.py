"""
Euler Project Problem #14
Longest Collatz sequence
http://projecteuler.net/problem=14
"""

def collatz(number):
    """This will take a number and apply the Collatz Conjecture.
    It returns the sequence of steps taken to reduce 'number' to 1.
    O(n)
    """
    
    sequence = [number]
    
    while number > 1:
        if number % 2 == 0:  # Even
            number /= 2
            sequence.append(number)
        else:
            number = 3 * number + 1  # Odd
            sequence.append(number)
    
    return sequence
            
def longest_collatz(limit):
    """Computes the longest Collatz Conjecture sequence from all numbers
    until 'limit'.
    O(n^2)
    """
    
    length = 1
    answer = 1
    
    for i in range(2, limit):
        if len(collatz(i)) > length:
            length = len(collatz(i))
            answer = i
    print """The number with the longest Collatz sequence under %d is
    %d. The sequence is %d steps long.
    """ % (limit, answer, length)

# Tests
longest_collatz(int(1E6))