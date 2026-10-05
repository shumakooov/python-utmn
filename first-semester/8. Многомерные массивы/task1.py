# Для каждой четной строки массива вычислить среднеарифметическое четных элементов кратных 10.

array = [
    [45, -32, 77, -10, 88],
    [-55, 20, -91, 30, 62],
    [90, -15, 40, 75, -80],
    [25, 60, -47, 10, 95],
]

for i in range(len(array)):
    if (i+1) % 2 == 0:
        row = array[i]
        target_elements = [x for x in row if x % 2 == 0 and x % 10 == 0]
        
        if target_elements:
            amount = 0
            for x in target_elements:
                amount += x
            avg = amount / len(target_elements)
            print(f"Строка {i + 1}, среднее: {avg}")
        else:
            print(f"Строка {i + 1}: нет элементов кратных 10")

print()
print("Исходный массив:")
for row in array:
    print(row)
print()

