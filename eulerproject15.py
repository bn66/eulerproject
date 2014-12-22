"""
Euler Project Problem #15
Lattice paths
http://projecteuler.net/problem=15
"""
import time
def lattice(size):
    """T
    O(???)
    """
    # up and right
    # psb = [[(0,0)]]
    psb = [[(1,0)],[(0,1)]]
    # if it's 1, print 2
    stop = 0
    len(psb)
    
    while True:
        for i in psb:
            # x,y coordinates of last point
            x = i[-1][0]
            y = i[-1][1]
            # print x, y
            
            if len(i) < size * 2: # less than maximum number of steps
                if x < size and y < size: # neither far right nor top
                    copy = list(i)
                    
                    i.append((x+1,y)) # move right
                    # print i, "i"
                    copy.append((x,y+1))  # move up
                    # print copy, "copy"
                    psb.append(copy)
                    # print psb
                    
                elif x == size and y < size: # farthest right, go straight up
                    for n in range(0, size-y):
                        # time.sleep(1)
                        i.append((x,y+(n+1)))
                    # print i
                    
                elif y == size and x < size: #farthest bottom
                    for n in range(0, size-x):
                        # time.sleep(1)
                        i.append((x+(n+1),y))
                    # print i
                    
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
lattice(4)