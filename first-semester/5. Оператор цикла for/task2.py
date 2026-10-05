# Напишите программу поиска трехзначных чисел, таких, что квадрат суммы трех цифр и квадрат этого числа оканчиваются на одну и ту же цифру.

import random

while True:
    num = random.randint(100,999)
    sum_digits = 0
    for i in str(num):
        sum_digits+= int(i)
    if sum_digits**2 % 10 == num**2 % 10:
        print(num)
        break
