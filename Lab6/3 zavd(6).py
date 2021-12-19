first_vect = list(map(float, input('Введіть координати першого вектора: ').split(' ')))
second_vect = list(map(float, input('Введіть координати другого вектора: ').split(' ')))

sum = 0

vect = []

if len(first_vect) == len(second_vect):

    for i in range(len(first_vect)):

        sum = first_vect[i] + second_vect[i]

        vect.append(sum)

print(vect)
