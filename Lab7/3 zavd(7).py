#Створити програму, для знаходження детермінанта квадратної матриці A(2x2)
A = []
n = 2
m = 2
for i in range(n):
    x = []
    for i in range(m):
        x.append(float(input('Введіть елементи матриці: ')))
    A.append(x)
determinant = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
print('Детермінант матриці = {0}'.format(determinant))
