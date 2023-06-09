# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_function(num1, num2):
    if num1 == 0:
        return num2
    else:
        return sum_function(num1 - 1, num2 + 1)

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))

print(f"Результатом суммы числа {A} и числа {B} будет {sum_function(A,B)}")