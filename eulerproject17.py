"""
Euler Project Problem #17
Number letter counts
http://projecteuler.net/problem=17
"""

def number_word(n):
    """
    
    Recursive
    Do not count spaces or hyphens. For example, 342 (three hundred and 
    forty-two) contains 23 letters and 115 (one hundred and fifteen)
    contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage.
    """
    # dictionary  two of them one for words one for letters
    value = None
    
    # numbers directly to values
    nums = {
        # Core numbers
        1: 3 # one
        2: 3 # two
        3: 5 # three
        4: 4 # four
        5: 4 # five
        6: 3 # six
        7: 5 # seven
        8: 5 # eight
        9: 4 # nine
        
        # Hard-coded
        10: 3 # ten
        11: 6 # eleven
        12: 6 # twelve
        20: 4 + 2 # twen + ty
        
        # suffixes
        'teen': 4
        'ty': 2
        
        # roots impure
        13: # thir + teen
        30: # thir + ty
        '3': 4 # thir-
        
        15: # fif + teen
        50: # fif + ty
        '5': 3 # fif-
        18: # eigh + teen
        80: # eigh + ty
        '8': 4 # eigh-
        # roots pure
        14: # four + teen
        40: # four + ty
        16: # six + teen
        60: # six + ty
        17: # seven + teen
        70: # seven + ty
        19: # nine + teen
        90: # nine + ty
        
        # 100: # one + hundred # and x -------------------------------------------------------
        # 1000: 3 + 8 # one + thousand 
    }
    
    # Length of number
    if n == 0:
        a == 0
    else:
        a = len(str(n))
        # a = math.floor(math.log10(n))+1 # faster
        
    # Number processing
    if a > 3 and a < 7: # thousands
        value += 8 # thousand
        value += number_word(n % 1000)
        return value
    elif a == 3: # hundreds
        value += nums[n // 100]
        value += number_word(n % 100)
        return value
    elif a == 2: # 10 through 99
        try:
            value += nums[n] # hard-coded: 10 11 12 20
        except KeyError:
            x = n // 10 # tens place
            y = n % 10 # ones place
            
            if x == 1: # 13 - 19
                
            elif x > 2: # Greater than 20
                
                value += number_word(y)
            elif:
            
    elif a == 1: # 1 through 9
        value += nums[n]
        return value
    elif a == 0:
        return 0
    else:
        print "Error"
        return None
    # elif  
    return value

def num_let_count(a, b):
    """Lit
    """
    sum = 0
    
    for i in range(a, b+1):
        sum += number_word(i)
    
    print """answer is:
        """
        
# tests
# num_let_count(1, 10)
# def number_word(100)