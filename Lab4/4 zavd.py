import math

A = float(input('Введіть значення A'))
C = float(input('Введіть значення C'))
N = float(input('Введіть значення N'))
if A == C == N:
    result = math.cos(A + C + N)
    print('{0}'.format(result))
elif A < C == N:
    result = math.cos(A*C*N)
    print('{0}'.format(result))
elif A < C < N:
    result = math.cos((A + C)* N)
    print('{0}'.format(result))
else:
    result = 0
    print('y = {0}'.format(result))