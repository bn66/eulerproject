"""
Euler Project Problem #4
Largest Palindrome Product
http://projecteuler.net/problem=4
"""

import time

def PalindromeTest(number):
    """This function will test if a number is a Palindrome.
    From the outside in, it compares the numbers.
    It returns a of True or False
    """
    list = map(int, str(number))  # create a list of digits
    for i in xrange(0, int(len(list) // 2) + 1):
        if list[i] == list[int(len(list) - 1) - i]: # outside-in
            continue
        else:
            return False
    return True
        
def Palindrome(digits):
    """This Function prints out the highest Palindrome and its 
    respective factors. It searches for all permutations of a
    specified amount of digits
    """
    Largest = 1 # intialize variables
    Factor0 = 1
    Factor1 = 1
    
    # set the bounds for searching
    for x in xrange(10 ** (digits - 1), 10 ** digits):
        for y in xrange(10 ** (digits - 1), 10 ** digits):
            if PalindromeTest(x * y) == True and x * y > Largest: 
                # test loop
                Largest = x * y
                Factor0 = x
                Factor1 = y
    print """The largest palindrome number as a result of the product
        of %d digit numbers is %d. Its factors are %d and %d. 
        """ % (digits, Largest, Factor0, Factor1)

def PalindromeTD(digits):
    """This Function prints out the highest Palindrome and its 
    respective factors. It attempts to minimize search time through a
    Top-Down approach; it will calculate with larger numbers first.
    O(n^1)
    """
    # intialize variables
    Largest = 1 
    Factor0 = 1
    Factor1 = 1
    
    # set the bounds for testing
    xHigh = 10 ** digits - 1 
    yHigh = 10 ** digits - 1
    xLow = 10 ** (digits - 1)
    yLow = 10 ** (digits - 1)
    
    # initialize the indices
    x = xHigh 
    y = yHigh
    
    while x > xLow: # start at top & count down
        if x * y > Largest: # avoids unnecessary values of x
            if PalindromeTest(x * y) == True: # check for Palindrome
                Largest = x * y # update
                Factor0 = x
                Factor1 = y
                y = yHigh # reset y & count down
                x += -1 
            elif y == yLow: # reached lower y limit without Palindrome
                y = yHigh
                x += -1
            else: # not Palindrome
                y += -1 
        else: # not worth checking
            y = yHigh
            x += -1

    print """The largest palindrome number as a result of the product
        of %d digit numbers is %d. Its factors are %d and %d. 
        """ % (digits, Largest, Factor0, Factor1)

# time tests        
tic = time.clock()
PalindromeTD(3)
toc = time.clock()
print "%f Top-Down time" % (toc - tic)

tic = time.clock()
Palindrome(3)
toc = time.clock()
print "%f Brute-Force time" % (toc - tic)