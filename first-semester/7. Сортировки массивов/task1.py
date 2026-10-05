# Используя алгоритмы сортировки напишите программу сортировки
# массива из N элементов (N вводиться с клавиатуры) следующим образом:
# отсортировать массив по не убыванию с помощью алгоритма сортировки
# «пузырек» до элемента массива, индекс которого вводиться с клавиатуры
# (необходимо осуществить проверку введенного индекса 0 < i< N-1), оставшуюся часть массива отсортировать по не возрастанию с помощью алгоритма сортировки массива выбором. Заполнение массива осуществить случайным образом целыми числами.

import random

def bubble_sort(arr, end_index):
    n = end_index + 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort_desc(arr, start_index):
    n = len(arr)
    for i in range(start_index, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

N = int(input("Введите размер массива N: "))

arr = [random.randint(-100, 100) for _ in range(N)]
print(f"\nИсходный массив: {arr}")

while True:
    try:
        i = int(input(f"\nВведите индекс разделения i (0 < i < {N-1}): "))
        if 0 < i < N - 1:
            break
        else:
            print(f"Индекс должен быть в диапазоне: 0 < i < {N-1}")
    except ValueError:
        print("Пожалуйста, введите целое число!")

bubble_sort(arr, i)
print(f"После сортировки пузырьком до индекса {i}: {arr}")

selection_sort_desc(arr, i + 1)
print(f"После сортировки выбором от индекса {i+1}: {arr}")
