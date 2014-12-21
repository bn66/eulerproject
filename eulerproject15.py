"""
Euler Project Problem #15
Lattice paths
http://projecteuler.net/problem=15
"""

def lattice(size):
    """T
    O(???)
    """
    
    # psb = [[(0,0)]]
    psb = [[(0,0),(1,0)],[(0,0),(0,-1)]]
    # if it's 1, print 2
    stop = 0
    len(psb)
    
    while True:
        for i in psb:
            # x,y coordinates of last point
            x = i[-1][0]
            y = i[-1][1] 
            # print x, y
            
            if len(i) < size * 2: # less than maximum possible steps
                if x < size and y > -size: # neither far right nor bottom
                    copy = list(i)
                    
                    i.append((x+1,y)) # move right
                    # print i, "i"
                    copy.append((x,y-1))  # move down
                    # print copy, "copy"
                    
                    psb.append(copy)
                    # print psb
                    
                elif x == size: # farthest right
                    # print "reached max x"
                    i.append((x,y-1))
                    # for n in range(y, size):
                        # i.append((x,y-1))
                    
                elif y == -size: #farthest bottom
                    # print "reached max y"
                    i.append((x+1,y))
                else:
                    print "Error"
                    return None
            else: 
                if len(i) == size*2:
                    stop += 1
                    # print stop
                    if stop == len(psb):
                        print "size of psb is", stop
                        return None
                else: 
                    stop = 0

                # move completed items to a different list
lattice(2)