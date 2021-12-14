
a = float(input('Дійсне число: '))
n = int(input('Натуральне число: '))
x = 2
result = a
while x<n:
    result = result*(a+(x-1))
    x+=1
print(result)

