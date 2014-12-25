nums = {'3': 'working'}

x = 3

try:
    nums[str(x)]
except KeyError:
    pass
    
print "thing"