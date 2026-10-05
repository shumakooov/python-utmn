# Цель эксперимента
# Сравнительный анализ эффективности трех алгоритмов сортировки (пузырьковой, выбором и вставкой) на массивах различного размера по времени выполнения и количеству операций перестановки.

# Входные параметры
# Размеры тестовых массивов:
# •	100 элементов
# •	1000 элементов
# •	10000 элементов

# Тип данных: вещественные числа в диапазоне [-1000, 1000]

# Количество запусков: по 5 запусков для каждого алгоритма и каждого размера массива

# Выходные параметры
# Измеряемые метрики:
# •	Время выполнения сортировки (в секундах)
# •	Количество операций перестановки элементов

# Процессор — AMD Ryzen 5 4600H (6 ядер, 12 потоков, штатная частота – 3 ГГц, максимальная частота в Turbo-режиме — 4 ГГц, Cache L3 — 8 МБ)
# Оперативная память — 16 ГБ DDR4-2666 МГц

import time
import random

def generate_random_array(size):
    """Генерация массива случайных вещественных чисел"""
    return [random.uniform(-1000, 1000) for _ in range(size)]

def bubble_sort(arr):
    """Пузырьковая сортировка"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    swap_count = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swap_count += 1
    return arr_copy, swap_count

def selection_sort(arr):
    """Сортировка выбором"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    swap_count = 0
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            swap_count += 1
    return arr_copy, swap_count

def insertion_sort(arr):
    """Сортировка вставкой"""
    arr_copy = arr.copy()
    swap_count = 0
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
            swap_count += 1
        arr_copy[j + 1] = key
        if j + 1 != i:
            swap_count += 1
    return arr_copy, swap_count

def run_sorting_experiment():
    """Проведение эксперимента сортировки"""
    sizes = [100, 1000, 10000]
    algorithms = [
        ("Пузырьковая сортировка", bubble_sort),
        ("Сортировка выбором", selection_sort),
        ("Сортировка вставкой", insertion_sort)
    ]
    
    # Создаем массивы для каждого размера
    arrays = {}
    for size in sizes:
        arrays[size] = generate_random_array(size)
        print(f"Сгенерирован массив из {size} элементов")
    
    print("\n" + "="*50)
    
    results = {}
    
    for size in sizes:
        print(f"\nРезультаты для массива из {size} элементов:")
        print("-" * 40)
        
        test_array = arrays[size]
        size_results = {}
        
        for algo_name, algo_func in algorithms:
            print(f"\n{algo_name}:")
            best_time = float('inf')
            best_swaps = 0
            
            # 5 запусков для каждого алгоритма
            for run in range(5):
                start_time = time.time()
                sorted_array, swap_count = algo_func(test_array)
                elapsed_time = time.time() - start_time
                
                print(f"  Запуск {run + 1}: время = {elapsed_time:.6f} сек, перестановки = {swap_count}")
                
                # Сохраняем лучший результат
                if elapsed_time < best_time:
                    best_time = elapsed_time
                    best_swaps = swap_count
            
            size_results[algo_name] = {
                'best_time': best_time,
                'best_swaps': best_swaps
            }
            
            print(f"  Лучшее время: {best_time:.6f} сек")
            print(f"  Перестановок: {best_swaps}")
        
        results[size] = size_results
    
    return results

print("=" * 50)

# Проводим эксперимент
results = run_sorting_experiment()

# Выводим итоговые результаты
print("\n" + "="*60)
print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ (лучшее время из 5 запусков)")
print("="*60)

sizes = [100, 1000, 10000]
algorithms = ["Пузырьковая сортировка", "Сортировка выбором", "Сортировка вставкой"]

for size in sizes:
    print(f"\nРазмер массива: {size} элементов")
    for algo_name in algorithms:
        time_val = results[size][algo_name]['best_time']
        swaps = results[size][algo_name]['best_swaps']
        print(f"  {algo_name}: {time_val:.6f} сек, перестановок: {swaps}")


# Вывод
# Сортировка выбором показала наилучшие результаты и по количеству перестановок, и по времени на всех размерах массивов, значительно превосходя другие алгоритмы. Сортировка вставкой оказалась в два раза быстрее пузырьковой на массиве из 10000 элементов, но все еще хуже, чем сортировка выбором. Для больших массивов пузырьковая сортировка показала наихудшие результаты как по времени выполнения, так и по количеству перестановок.
