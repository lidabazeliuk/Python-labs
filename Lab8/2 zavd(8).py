a = list(map(float, input('Введіть координати вектора A: ').split(' ')))
b = list(map(float, input('Введіть координати вектора B: ').split(' ')))
c = list(map(float, input('Введіть координати вектора C: ').split(' ')))


def scalar_product(x, y):
    if len(x)==len(y):
        s = 0
        for i in range(len(x)):
            s += x[i] * y[i]
        return s
    else:
        print('Error')

result = 2 * (scalar_product(a, b)) - 3 * (scalar_product(a, c))
print('result = {0}'.format(result))