# import pandas as pd; print(pd.__version__)
# Replace all ______ with rjust, ljust or center. 

thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((2*i*c + c).center(2*thickness-1,' '))

# Top Pillars
for i in range(thickness+1):
    print((thickness*c).center(2*thickness-1,' ')+ (2*thickness+1)*' ' + (thickness*c).center(2*thickness-1,' '))

# Middle Belt
for i in range((thickness+1)//2):
    print((5*thickness*c).center(6*thickness,' '))

# Bottom Pillars
for i in range(thickness+1):
    print((thickness*c).center(2*thickness-1,' ')+ (2*thickness+ 1)*' ' + (thickness*c).center(2*thickness-1,' '))

# Bottom Cone 0,1,2,3,4
for i in range(thickness):
    print((4*thickness-1)*' ' + ((2*(thickness-i)-1)*c).center(2*thickness+ 1,' '))
    
