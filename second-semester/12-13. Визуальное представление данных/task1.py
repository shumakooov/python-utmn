# img/2.12-13.1.png

import csv
import numpy as np
import matplotlib.pyplot as plt

grades_list = []

with open("students_data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        subject = row[1].strip()
        grade = row[2].strip()

        if subject == "ПиОА":
            grades_list.append(grade)

unique_grades, counts = np.unique(grades_list, return_counts=True)

labels = unique_grades.tolist()
sizes = counts.tolist()

plt.figure(figsize=(7, 7))
plt.pie(
    sizes,
    labels=labels,
)

plt.title("Распределение оценок по предмету ПиОА")
plt.legend(labels, title="Оценки")

plt.show()
