import math
x = float(input('x = '))
e = float(input('e = '))
n = 1
sum = 0
numerator = (x - 1)
denominator = (x + 1)
mul = (2 * n - 1)
r = 1/(2 * n - 1)
while math.fabs((numerator/denominator) ** (2 * n - 1)) > e:
    sum = sum + (r * (numerator/denominator) ** (2 * n - 1))
    n += 1

sum = sum + 2
print('sum = {0}'.format(sum))
print('ln({0}) = {1}'.format(x,math.log(x)))
