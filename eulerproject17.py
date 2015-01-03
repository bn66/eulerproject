"""
Euler Project Problem #17
Number letter counts
http://projecteuler.net/problem=17
"""
import math

def number_word(n):
    """Recursively calculates the number of letters in spelling out a 
    number, n, returns the value. Spaces and hyphens are not counted, 
    and 'and' is used. For example, 342 (three hundred and forty-two) 
    returns 23 and 115 (one hundred and fifteen) returns 20.The use of 
    "and" when writing out numbers is in compliance with British usage.
    Works up to 999,999.
    O(1)
    """
    value = 0
    
    # Numbers directly to values
    nums = {
        # Core numbers
        1: 3, # one
        2: 3, # two
        3: 5, # three
        4: 4, # four
        5: 4, # five
        6: 3, # six
        7: 5, # seven
        8: 5, # eight
        9: 4, # nine
        
        # Hard-coded
        10: 3, # ten
        11: 6, # eleven
        12: 6, # twelve
        
        # Weird
        '20': 4 + 2, # twen + ty
        '40': 5, # for + ty
        
        # Impure roots
        '3': 4, # thir-
        '5': 3, # fif-
        '8': 4, # eigh-
    }
    # Length of number
    if n == 0:
        a = 0
    else:
        a = math.floor(math.log10(n)) + 1
        
    # Recursive Processing
    if a > 3 and a < 7: # Thousands
        value += number_word(n // 1000) + 8 # t-h-o-u-s-a-n-d
        value += number_word(n % 1000)
        return value
    elif a == 3: # Hundreds
        value += nums[n // 100] + 7 # h-u-n-d-r-e-d
        if n % 100 != 0:
            value += number_word(n % 100) + 3 # 'and'
        return value
    elif a == 2: # 10 through 99
        x = n // 10 # Tens place
        y = n % 10 # Ones place
        
        # Hard-coded: 10 11 12
        try:
            value += nums[n]
            return value
        except KeyError:
            pass
        
        # Weird
        if x == 2:
            value += nums['20'] # t-w-e-n-t-y
            value += number_word(y)
            return value       
        if x == 4: 
            value += nums['40'] # f-o-r + t-y
            value += number_word(y)
            return value
        
        if x == 1: # Teens, 13 through 19
            try:
                value += nums[str(y)] + 4 # Impure roots: 3 5 8 + -teen
                return value
            except KeyError:
                value += nums[y] + 4 # 4 6 7 9 + -teen
                return value        
        elif x >= 3: # 31 through 99
            try:
                value += nums[str(x)] + 2 # Impure roots: 3 5 8 + -ty
                value += number_word(y)
                return value
            except KeyError:
                value += nums[x] + 2 # 6 7 9 + -ty
                value += number_word(y)
                return value
    elif a == 1: # 1 through 9
        value += nums[n]
        return value
    elif a == 0:
        return 0

def number_word_loop(a, b):
    """Calls on number_word function to find the sum of letters in
    numbers written out from a to b.
    O(n)
    """
    sum = 0
    
    for i in range(a, b+1):
        sum += number_word(i)
    
    print """The total number of letters of all numbers from %d to %d
        written in words is %d
        """ % (a, b, sum)
        
# tests
number_word_loop(1, 1000)
# def number_word(100)
"""
Notes:
    # roots impure
    13: # thir + teen
    30: # thir + ty
    15: # fif + teen
    50: # fif + ty
    18: # eigh + teen
    80: # eigh + ty

    # roots pure
    14: # four + teen
    40: IMPURE
    
    16: # six + teen
    60: # six + ty
    17: # seven + teen
    70: # seven + ty
    19: # nine + teen
    90: # nine + ty
    
    # suffixes
    # 'teen': 4
    # 'ty': 2
"""