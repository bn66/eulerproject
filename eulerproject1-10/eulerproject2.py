"""
Euler Project Problem #2
Even Fibonacci numbers
http://projecteuler.net/problem=2
"""

# intialize first two & list
Fib = []
Fib.append(1)
Fib.append(2)

# generate Fib numbers
while Fib[-1] < int(4E6):
    Fib.append(Fib[-1] + Fib[-2])

# remove last iteration of while loop
Fib.pop(-1)
print Fib # double check

#intialize
sum_list = []
j = 0

for i in Fib:
    if Fib[j] % 2 != 0:   # if odd
        j += 1
    else:
        sum_list.append(Fib[j]) # add the even
        j += 1
        
    
print sum(sum_list)

# O(n)

# finding the nth Fibonacci number using a recursive function
# for fun
def FibFind(one, two, nth):
    if nth == 2: #off set
        return two
    else:
        return FibFind(two, one + two, nth - 1)
        

print FibFind(1, 2, 8) # test case