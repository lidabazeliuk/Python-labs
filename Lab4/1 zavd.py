import math

A_x = float(input('Введіть координату точки A по x'))
A_y = float(input('Введіть координату точки А по y'))
B_x = float(input('Введіть координату точки B по x'))
B_y = float(input('Введіть координату точки B по y'))
C_x = float(input('Введіть координату точки C по x'))
C_y = float(input('Введіть координату точки C по y'))

AB = math.sqrt((B_x - A_x) ** 2 + (B_y - A_y) ** 2 )
BC = math.sqrt((C_x - B_x) ** 2 + (C_y - B_y)**  2 )
AC = math.sqrt((C_x - A_x) ** 2 + (C_y - A_y)**  2 )

p = (AB + BC + AC)/2
S = math.sqrt(p*(p - AB)*(p - BC)*(p - AC))
print(S)