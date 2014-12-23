"""
Euler Project Problem #17
Number letter counts
http://projecteuler.net/problem=17
"""

def number_word(a, n):
    """Lit
    """
    
    # dictinary  two of them one for words one for letters
    
    list = map(int, str(a ** n))
    ans = sum(list)
    
    print ans

# tests
# power_sum(2,1000)