def number_of_Fibonacci(x):
    if x < 0:
        print('Error')
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return number_of_Fibonacci(x-1) + number_of_Fibonacci(x - 2)

result = number_of_Fibonacci(3) + number_of_Fibonacci(8)
print('result = ',result)