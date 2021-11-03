x = float(input('x = '))
y = float(input('y = '))
n = int(input('Введіть кількість елементів списку '))
z = float(input('z = '))

mass = [x, x, y]
i = 4
if n == 1:
    mass.append(x)
elif n == 2:
    mass += [x , x]
elif n == 3:
    mass += [x, x, y]
elif n >= 4:
    mass += [x, x, y]
    print(mass)
    while n > i:
        a_i = mass[i - 2] + (mass[i - 1] / 2 ** (i - 1)) * mass[i - 3]
        mass.append(a_i)
        i = i + 1
print('елементи списка = {0}'.format(mass))
list1 = []
for j in mass:
    if j > z:
        list1.append(j)

print('елементи які більші за z = {0}'.format(list1))
