n = int(input('number = '))
num = 1
while n > 9:
    n = n//10
    num += 1
print('num = {0}'.format(num))
