from Functions_Library import *

# Exercise 1

print(Point(2,1) == Point(2,1.1))
print(Point(2,1) == Point(2,1.000001))
print(Point(2,3,5) == Point(1.9999999,3.0000001, 5))
print(Point(1,2,3,4,5) == Point(1,3,2,4,5))
print(Point(0,0) == Point(0,0,0))