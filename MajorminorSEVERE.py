import sys
number = (int) ( sys.argv[1])
#print(number)
if number < 50 and number > 0:
    print 'Minor'
elif number >= 50 and number <100:
    print 'Major'
else:
    print 'Severe'

