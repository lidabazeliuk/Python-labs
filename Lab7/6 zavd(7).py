#Дана цілочислова прямокутна матриця. Визначити максимальне із чисел, яке зустрічається в даній матриці більше одного разу.
a = []
n = int(input('Введіть кількість рядків: '))
m = int(input('Введіть кількість стовпців: '))
for i in range(n):
    f = []
    for i in range(m):
        f.append(float(input('Введіть елементи матриці: ')))
    a.append(f)
list = []
for n in a:
    list.extend(n)
i = max([el for el in list if list.count(el)>1])
print('Найчастіше зустрічається число: {0}'.format(i))
