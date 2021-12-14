n = int(input('Введіть кількість елементів: '))
x = int(input('Початковий елемент:'))
list1=list(range(x,x+n))
print(list1)
print('Середнє арифметичне значення = {0}'.format(sum(list1)/len(list1)))

