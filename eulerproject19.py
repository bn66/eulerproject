"""
Euler Project Problem #19
Counting Sundays
http://projecteuler.net/problem=19
"""

def sunday_count(year):
    """Counts first sundays based on first day of year
    O(???)
    """
    # first_day = year
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    sundays = 0 # Number of Sundays
    
    months = [('Jan',31), ('Feb',28), ('Mar',31), ('Apr',30), 
        ('May',31), ('Jun',30), ('Jul',31), ('Aug',31), 
        ('Sep',30), ('Oct',31), ('Nov',30), ('Dec',31)]
    if year % 4 == 0 and year % 400 != 0: # Leap year
        months[1] = ('Feb',29)
        # print "leap year"
    
    # first day
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
    
    
def first_day(year):
    """Input is a year number
    Return first day of given year, 
    O(???)
    """
    # 1 Jan 1900 was a Monday
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    # Moves by 1 day for or 2 for leep years
    day = 1 # Monday in 1900
    day += (year - 1900)
    if year > 1900:
        day += (year - 1901) // 4        
    day = day % 7
    return day
    # return days[day]
    
# generate first dates
a = 0
for i in range(1901, 1905):
    a += sunday_count(i)
    # a += sunday_count(first_day(i))
    # print i, first_day(i)
    
print a
    
