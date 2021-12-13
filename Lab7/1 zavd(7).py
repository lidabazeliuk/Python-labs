#Визначити суму від’ємних елементів матриці з обома парними індексами
A = []
n = int(input('Введіть кількість рядків: '))
m = int(input('Введіть кількість стовпців: '))
sum = 0
for i in range(n):
    f=[]
    for i in range(m):
        f.append(float(input('Введіть елементи матриці: ')))
    A.append(f)
for j in range(n):
    for i in range(m):
        if j%2==0 and i%2==0 and A[j][i]<0:
            sum += A[j][i]
print(sum)