"""
Euler Project Problem #1
Multiples of 3 and 5
http://projecteuler.net/problem=1
"""

import time

# Method 1 -  Summation:

tic = time.clock()

three_sum = 0 # initialize
five_sum = 0
correction_sum = 0

upper_limit = 1E3 - 1 # below/not including
three_limit = upper_limit // 3
five_limit = upper_limit // 5
correction_limit = upper_limit // 15

# summation formula for i from 1 to n is n*(n+1)/2
three_sum = 3 * (three_limit) * (three_limit + 1) / 2 
five_sum = 5 * (five_limit) * (five_limit + 1) / 2 
correction_sum = (3 * 5) * (correction_limit) * (correction_limit + 1) / 2
# correction_sum accounts for dupes

answer = three_sum + five_sum - correction_sum
print answer

toc = time.clock()
print toc - tic # Computes Quicker



# Method 2 - For-loop:

tic = time.clock()
sum = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print sum
    
toc = time.clock()
print toc - tic # Computes Slower