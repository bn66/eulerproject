"""
Euler Project Problem #15
Lattice paths
http://projecteuler.net/problem=15
"""

def lattice(size):
    """T
    O(???)
    """
    # ordered dictionary?
    
    # psb = [[(0,0)]]
    psb = [[(0,0),(1,0)],[(0,0),(0,-1)]]
    # if it's 1, print 2
    while True:
        for i in psb:
            # print i
            # print size**2
            if len(i) < size*2:
                print "in if"
                if i[-1][0] < size or i[-1][1] < size:
                    # print "first", i[-1][0]
                    # print "second", i[-1][1]
                    
                # if # last entry in i is less than the length or width # absolute value
                # set[0]
                # elif:
                    # add 0
                # i.append(i)
    print psb
	




lattice(2)