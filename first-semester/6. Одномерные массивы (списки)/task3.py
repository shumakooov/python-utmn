# Дан одномерный массив, получить другой массив той же размерности,
# каждый элемент которого равен bi = a1 + a2 + ... + ai

my_list = [1, 9, 12, 56, 23, 100, 21, 2, 7, 63, 126, -125, -1, -5]
new_list = []

for i in range(len(my_list)):
    new_element = 0
    for j in range(i+1):
        new_element+= my_list[j]
    new_list.append(new_element)

print(f"Новый массив: {new_list}")
print(f"Старый массив: {my_list}")
