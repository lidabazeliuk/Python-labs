matrix = []
n = int(input('Введіть кількість рядків: '))
m = int(input('Введіть кількість стовпців: '))
num = 1
x = 0
for i in range(n):
    f = []
    for j in range(m):
        if (j * i) % 2 == 0:
            for y in range(m+1):
                num *= y
            f.append(num)
        else:
            for y in range (n + 1):
                x += y
            f.append(x)
    matrix.append(f)
print(matrix)

list = []
for el in matrix:
    list.extend(el)
print(list)