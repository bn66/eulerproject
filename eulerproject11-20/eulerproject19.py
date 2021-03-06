"""
Euler Project Problem #19
Counting Sundays
http://projecteuler.net/problem=19
"""

def sunday_count(year):
    """Given a year, counts the number of first sundays.
    O(???)
    """
    # first_day = year
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    sundays = 0 # Number of Sundays
    
    months = [('Jan',31), ('Feb',28), ('Mar',31), ('Apr',30), 
        ('May',31), ('Jun',30), ('Jul',31), ('Aug',31), 
        ('Sep',30), ('Oct',31), ('Nov',30), ('Dec',31)]
        
    if year % 400 == 0: # Unless divisible by 400
        months[1] = ('Feb',29)
    elif year % 4 == 0 and year % 100 != 0: # 4 years, not on century
        months[1] = ('Feb',29)
        # print "leap year"
    
    # first day of the year
    # Moves by 1 day for or 2 for leep years
    day = 1 # Monday in 1900
    day += (year - 1900)
    if year > 1900:
        day += (year - 1901) // 4        
    day = day % 7
    # return day    
    first_day = day
    
    for month in months:
        first_day += month[1] % 7
        first_day = first_day % 7
        if first_day == 0:
            sundays += 1
        print month[0], days[first_day], year
        
    return sundays
    
# generate first dates
a = 0
for i in range(1901, 2001):
    a += sunday_count(i)
    
print a
    
