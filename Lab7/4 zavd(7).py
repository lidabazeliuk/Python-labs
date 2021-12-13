#Розмістити елементи парних рядків у порядку зростання.
a = []
n = int(input('Введіть кількість рядків: '))
m = int(input('Введіть кількість стовпців: '))
for i in range(n):
    f = []
    for i in range(m):
        f.append(float(input('Введіть елементи матриці: ')))
    a.append(f)

print(a)

for j in a:
    if a.index(j)%2 != 0:
        j.sort()
        print(j)
    else:
        continue