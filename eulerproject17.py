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
    value = 0
    
    # numbers directly to values
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
        # 20f;lkafj;ljjjjjjjjjjjjjjjjjjjjjjjjj
        20: 4 + 2, # twen + ty
        
        # roots impure
        '3': 4, # thir-
        '5': 3, # fif-
        '8': 4, # eigh-
        '40': 3, # for-
        
        
        # 1000: 3 + 8 # one + thousand 
    }
    
    # Length of number
    if n == 0:
        a = 0
    else:
        a = len(str(n))
        # a = math.floor(math.log10(n))+1 # faster
        
    # Number processing
    if a > 3 and a < 7: # thousands
        value += 8 # t-h-o-u-s-a-n-d
        value += nums[n // 1000]
        value += number_word(n % 1000)
        return value
    elif a == 3: # hundreds
        value += nums[n // 100] + 7 # h-u-n-d-r-e-d
        if n % 100 != 0:
            value += number_word(n % 100) + 3 # 'and'
        else:
            value += 0
        return value
    elif a == 2: # 10 through 99
        x = n // 10 # tens place
        y = n % 10 # ones place
        
        try:
            value += nums[n] # hard-coded: 10 11 12 20 **************
            return value
        except KeyError:
            pass
        
        if x == 4: # forty and fourteen are different
            value += nums['40'] + 2 # f-o-r + t-y
            value += number_word(y)
            return value
        if x == 1: # Teens, 13 through 19
            try:
                value += nums[str(y)] + 4 # impure roots: 3 5 8 + -teen
                return value
            except KeyError:
                value += nums[y] + 4 # 4 6 7 9 + -teen
                return value            
        elif x >= 2: # 21?????????????? through 99
            try:
                value += nums[str(x)] + 2 # impure roots: 3 5 8 + -ty
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
    else:
        print "Error"
        return None
    return value

def num_let_count(a, b):
    """Lit
    """
    sum = 0
    
    for i in range(a, b+1):
        sum += number_word(i)
    
    print """answer is:
        """, sum
        
# tests
num_let_count(1, 1000)
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