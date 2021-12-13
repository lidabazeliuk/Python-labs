#Дана цілочислова прямокутна матриця. Визначити кількість рядків, які не містять жодного нульового елемента.
a = []
n = int(input('Введіть кількість рядків: '))
m = int(input('Введіть кількість стовпців: '))
for i in range(n):
    f = []
    for i in range(m):
        f.append(float(input('Введіть елементи матриці: ')))
    a.append(f)
x = 0
if n != m:
    for el in a:
        print(el)
        for l in el:
            if l == 0:
                x += 1
                break
            else:
                continue
else:
    print('Матриця не прямокутна')

print('Кількість рядків,які без нульового елемента = {0}'.format(n-x))