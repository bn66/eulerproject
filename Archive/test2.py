def product(List):
    """Returns the product of every item in a list
    O(n)
    """
    product = 1
    for i in List:
        product *= i
    else:
        return product
        
def product_2(list):
    reduce(lambda x, y: x * y, list)
    

numbers = [range(1,int(10))]
numbers_2 = [range(1,int(1E3))]
numbers_3 = [range(1, 100000000)]

import time    


tic = time.clock()
product(numbers)
toc = time.clock()
print toc - tic, "iter, small list"

tic = time.clock()    
product_2(numbers)
toc = time.clock()
print toc - tic, "reduce, small list"

tic = time.clock()
product(numbers_2)
toc = time.clock()
print toc - tic, "iter, med list"

tic = time.clock()    
product_2(numbers_2)
toc = time.clock()
print toc - tic, "reduce, med list"

tic = time.clock()
product(numbers_3)
toc = time.clock()
print toc - tic, "iter, large list"

tic = time.clock()    
product_2(numbers_3)
toc = time.clock()
print toc - tic, "reduce, large list"