"""
Euler Project Problem #18
Number letter counts
http://projecteuler.net/problem=18
"""
import math

def number_word(n):
    """Recursively calculates the number of letters in spelling out a 
    number, n, returns the value. Spaces and hyphens are not counted, 
    and 'and' is used. For example, 342 (three hundred and forty-two) 
    returns 23 and 115 (one hundred and fifteen) returns 20.The use of 
    "and" when writing out numbers is in compliance with British usage.
    O(1)
    """
    # dictionary  two of them one for words one for letters
    value = 0
  
# tests
number_word_loop(1, 1000)
# def number_word(100)