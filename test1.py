'''
Created on Apr 26, 2018

@author: joclark
'''
# Edit from jfclarkjruser
# Second edit from jfclarkjruser
# Third comment
import math
import random

if __name__ == '__main__':
    pass

print('Herro')

# Some arithmetic
a=1
b=21
c = a + b
print(c)

# if/else statements
if b < a:
    print('b is less than a!')
else:
    print('a is less than b!')
    if b == 20:
        print('b is 20!')
    else:
        print('b is not 20!')

# While loops
while a < b:
    print('The value of a is now: {}'.format(a))
    a += 1

# Cast the value of c as a float value
d = float(c)
print(d)

# Square root
print(math.sqrt(81))

# Some random numbers
print('Random number examples')
print(random.random())
print(random.randint(1, 100))


