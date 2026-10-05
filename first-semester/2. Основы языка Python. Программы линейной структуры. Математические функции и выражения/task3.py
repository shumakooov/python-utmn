# Является ли сумма цифр четырехзначного положительного числа
# четным числом.

number = input("Введите число -> ")
sum = 0
for i in str(number):
    sum += int(i)
isEven = sum % 2 == 0
print(isEven)
