from collections import namedtuple

n = int(input())
labels = input().split()

ind = labels.index("MARKS")

point = namedtuple('point',['MARKS'])

sum = 0
for i in range(0,n):
    records = input().split()
    p1 = point(MARKS = int(records[ind]))
    sum+= p1.MARKS

print(f'{sum/n:.2f}')
    

'''
print(p1.x)
print(p2.x)

Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price=10000, Mileage=30, Colour="Cyan", Class="Y")
print(xyz.Class)
'''