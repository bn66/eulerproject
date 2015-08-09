"""
Euler Project Problem #15
Lattice paths
http://projecteuler.net/problem=15
"""
from math import factorial

def lattice_bf(sizex, sizey = None):
    """Brute force method for finding all paths in a rectangular
    lattice. Arguments must be integers greater than zero. This method
    becomes exponentially slower. Note that this method travels right
    and upwards, as opposed to downwards and to the right.
    O(n^2)
    """
    # up and right
    psb = [ [(1,0)], [(0,1)] ] # possibilities
    stop = 0
    answers = []
    if sizey == None: # square
        sizey = sizex
    
    while True:
        for i in psb:
                
            # x,y coordinates of last point
            x = i[-1][0]
            y = i[-1][1]
            
            if len(i) < sizex + sizey: # less than max steps
            
                if x < sizex and y < sizey: # neither far right nor top
                    copy = list(i)
                    
                    i.append((x+1,y)) # move right
                    copy.append((x,y+1))  # move up
                    psb.append(copy)
                elif x == sizex and y < sizey: # farthest right, go up
                    for n in range(0, sizey-y):
                        i.append((x,y+(n+1)))
                        # print i
                elif y == sizey and x < sizex: # farthest top, go right
                    for n in range(0, sizex-x):
                        i.append((x+(n+1),y))
                        # print i
                else:
                    print "Error"
                    return None

            else: 
                 if len(i) == sizex + sizey:
                    stop += 1
                    answers.append(i)
                    psb.remove(i)
                    if len(psb) == 0:
                        # print "All possible steps is", answers
                        print """The maximum number of paths in a 
                            %d by %d square lattice is %d
                            """ % (sizex, sizey, stop)
                        return None

def lattice_add(sizex, sizey = None):
    """Method for finding all paths in a rectangular lattice based on 
    discovered numerical patterns. This is significantly faster than the
    brute force method although having the same time complexity.
    O(n^2)
    """
    mx = max(sizex, sizey)
    # mn = min(sizex, sizey)
    list = [[]]
    if sizey == None: # square
        sizey = sizex
        
    for i in range(1, mx+1): # first row
        list[0].append(i+1)
    for i in range(2, mx+1): # first column
        list.append([i+1])        
    
    # remaining rows, by adding the previous number + the above
    for i in range(1, mx): 
        for j in range(1, mx):
            list[i].append( list[i][-1] + list[i-1][j] ) # prev + above
    
    # print list
    print """The maximum number of paths in a %d by %d lattice is %d
        """ % (sizex, sizey, list[sizex-1][sizey-1])

def lattice_cmb(size):
    """Equation for finding all paths in a rectangular lattice using
    combinatorics.
    O(1)
    """
    
    answer = factorial(2*size) / (factorial(size) ** 2)
    
    print """The maximum number of paths in a %d by %d square lattice 
        is %d
        """ % (size, size, answer)

# lattice_bf(2,2)        
# lattice_add(20)
# lattice_cmb(20)