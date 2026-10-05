# Вычислить среднее арифметическое положительных элементов
# массива и вывести на экран элементы больше среднего.

my_list = [1, 9, 12, 56, 23, 100, 21, 2, 7, 63, 126, -125, -1, -5]

amount = 0
count_positive = 0

for i in my_list: 
    if i > 0:
        amount+= i
        count_positive+= 1

average = amount / count_positive

for i in my_list:
    if i > average:
        print(i)

print(f"Весь массив: {my_list}")
