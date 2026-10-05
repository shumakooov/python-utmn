# Для элементов массива, находящихся в четных строках и нечетных столбцах найти среднее арифметическое элементов кратных 5 и вывести на экран все элементы массива больших среднего и их индексы

array = [
    [45, -32, 77, -10, 88],
    [-55, 20, -91, 30, 62],
    [90, -15, 40, 75, -80],
    [25, 60, -47, 10, 95],
]

count = 0
total = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        if i % 2 == 0 and j % 2 == 1:
            if array[i][j] % 5 == 0:
                total += array[i][j]
                count += 1

if count > 0:
    avg = total / count
else:
    avg = 0

print(f"Среднее арифметическое элементов кратных 5 в четных строках и нечетных столбцах: {avg}")

print("\nЭлементы больше среднего и их индексы:")
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > avg:
            print(f"array[{i}][{j}] = {array[i][j]}")

print()
print("Исходный массив:")
for row in array:
    print(row)
print()
