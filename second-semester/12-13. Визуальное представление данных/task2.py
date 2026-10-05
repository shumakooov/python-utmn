# Имеется файл students_data.csv, в котором через запятую хранится следующая информация:
# ФИ студента, Предмет, Оценка, ФИО преподавателя, Специальность. Необходимо
# написать программу на языке Python, которая строит столбчатую диаграмму
# по студенту Иван Козлов с выводом количества оценок разного вида.

import csv
import numpy as np
import matplotlib.pyplot as plt

grades_list = []

with open("students_data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        full_name = row[0].strip()
        grade = row[2].strip()

        if "Иван Козлов" in full_name or "Козлов Иван" in full_name:
            grades_list.append(grade)

unique_grades, counts = np.unique(grades_list, return_counts=True)

labels = unique_grades.tolist()
sizes = counts.tolist()

plt.figure(figsize=(7, 7))
plt.bar(
    labels,
    sizes,
)

plt.title("Статистика оценок студента Ивана Козлова")
plt.legend(labels, title="Оценки")

plt.show()
