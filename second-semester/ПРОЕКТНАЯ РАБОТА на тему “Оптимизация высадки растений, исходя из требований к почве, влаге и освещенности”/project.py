# Введение:
# В некоторой ландшафтной студии приходилось вручную искать информацию о экологических факторах растений,
# которые можно внести в проект на озеленение частных территорий в Тюмени, что занимало много времени.
# Руководитель придерживается мнения, что ИИ часто ошибается, а в этом деле ошибка в выборе растений является
# самой опасной и ключевой.
# В решении этой проблемы заинтересованы также другие ландшафтные студии, биологи, экологи, ботаники
# и просто любители садоводства. Это поможет в правильном выборе растений, что будет приводить к успешной
# высадке и приживанию растений.

# Проблема:
# В выборе растений для своего участка нужно учитывать не только свои предпочтения в красоте растения,
# но и условия необходимые ему, что для новичков или не разбирающихся в данной теме является проблемой. 
# Чаще всего плохо выбранные растения не приживаются, требуя много внимания и сил чтобы себя оживить,
# а также могут вытеснить существующие культуры на участке

# Актуальность:
# В самом разгаре сезона озеленения своих участков ландшафтные дизайнеры и просто любители смогут
# создавать список растений для высадки, подбирая его благодаря жизненным факторам растений и их
# совместимостью с условиями на их участке

# Цель:
# Разработать программу, которая будет показывать список растений, произрастающих в Тюмени, их жизненные
# формы и предпочтения к освещенности, влаге и почве, с помощью которой можно будет подобрать растения
# для своего участка по его факторам.

# Задачи:
# 1. Сформировать dataset. Собрать данные из интернета о растениях Тюменской области с помощью научных статей
# 2. Проанализировать данные. Выявить основные для озеленения участка, распределить по экологическим факторам
# (свет, влага, вода) и жизненным формам
# 3. Предобработать данные. Очистить выбросы, обработать пропуски
# 4. Разработать программу. 4 типа графиков для визуализации экологических групп и консольную программу для
# подбора растений по экологическим факторам
# 5. Оформить результаты





# Сбор датасета:
# Всю информацию о растениях, жизненных формах и экологических факторах я брала из следующих источников:
# https://www.inaturalist.org/guides/9746
# https://ru.ruwiki.ru/wiki/Жизненные_формы_растений:_деревья,_кустарники,_кустарнички,_многолетние_травы,_однолетние_травы
# https://studfile.net/preview/16457649/page:31/
# https://studfile.net/preview/9567349/
# https://studfile.net/preview/9567349/page:2/

# Разработка программы:
# Импортирую библиотеки: pandas для анализа данных, matplotlib для графиков и numpy для операций с массивами и числами.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Для начала считываю файл data.csv, в котором хранится датасет, и сохраняю его в переменную.

df = pd.read_csv('data.csv', sep=';')

# Далее перейдем к созданию первой диаграммы. Это столбчатая диаграмма, которая показывает 
# количество растений, принадлежащих к определенному типу почвы.
# В переменную soil_counts сохраняю количество упоминаний каждого из типов почвы и сортирую
# их в порядке убывания. После этого создаю саму диаграмму и задаю ей названия, а также названия
# осей. В цикле for задаю числовую подпись над каждым столбцом. Диаграмма готова, отображаю её и
# указываю plt.tight_layout() для автоматических отступов.

soil_counts = df['Почва'].value_counts().sort_values(ascending=False)

plt.bar(soil_counts.index, soil_counts.values, color='#77DD77', edgecolor='black')

plt.xlabel('Тип почвы', fontsize=12)
plt.ylabel('Количество растений', fontsize=12)
plt.title('Распределение растений по типам почвы', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

for i in range(len(soil_counts)):
    height = soil_counts.values[i]
    plt.text(i, height, f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# Перейдем к созданию горизонтальной диаграммы, которая показывает количество растений, принадлежащих
# к определенному типу освещенности. В переменную light_counts сохраняю количество упоминаний каждого
# из типов света и сортирую их в порядке возрастания. Как и в прошлом случае далее создаю саму
# диаграмму и задаю ей названия, а также названия осей. В цикле for задаю числовую подпись справа
# от каждой строки. Диаграмма готова, отображаю её и указываю plt.tight_layout() для автоматических отступов.

light_counts = df['Свет'].value_counts().sort_values(ascending=True)

plt.barh(light_counts.index, light_counts.values, color='#77DD77', edgecolor='black')

plt.xlabel('Количество растений', fontsize=12)
plt.ylabel('Тип света', fontsize=12)
plt.title('Распределение растений по типам света', fontsize=14, fontweight='bold')
plt.tick_params(axis='x', labelsize=10)
plt.tick_params(axis='y', labelsize=10)

for i in range(len(light_counts)):
    width = light_counts.values[i]
    plt.text(width, i, f'{int(width)}', ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()

# Следующим создаю график, который отображает количество растений, принадлежащих к определенному
# типу влаги. По аналогии с прошлыми двумя графиками в переменную moisture_counts сохраняю количество
# упоминаний каждого из типов влаги и сортирую их в порядке возрастания. Создаю график и задаю ему
# название, а также названия осей. Отображаю его и указываю plt.tight_layout() для автоматических отступов.

moisture_counts = df['Влага'].value_counts().sort_values(ascending=True)

plt.plot(moisture_counts.index, moisture_counts.values, linestyle='-', color='green')

plt.xlabel('Тип влаги', fontsize=12)
plt.ylabel('Количество растений', fontsize=12)
plt.title('Распределение растений по типам влаги', fontsize=14, fontweight='bold')
plt.tick_params(axis='x', labelsize=10)
plt.tick_params(axis='y', labelsize=10)
plt.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()

# Перейдем к созданию круговой диаграммы, отображающей количество растений принадлежащих к каждой из
# жизненных форм. В переменную lifeform_counts сохраняю количество упоминаний каждой из жизненной формы.
# Создаю диаграмму и получаю три объекта: wedges — сами секторы, texts — подписи категорий, autotexts —
# подписи значений. Wedges использую для добавления легенды, в которой растения указаны в формате
# “Жизненная форма: Количество”. Также показываю абсолютные числа (количество растений) в секторах,
# так как изначально доли показываются в процентах. Диаграмма готова, отображаю её и указываю
# plt.tight_layout() для автоматических отступов.

lifeform_counts = df['Жизненная форма'].value_counts()

wedges, texts, autotexts = plt.pie(
    lifeform_counts.values,
    labels=None,
    autopct=lambda p: f'{int(p/100 * lifeform_counts.sum())}',
    startangle=90,
    textprops={'fontsize': 10, 'fontweight': 'bold', 'color': 'white'}
)

plt.title('Распределение растений по жизненным формам', fontsize=14, fontweight='bold')

legend_labels = [f'{label}: {count}' for label, count in zip(lifeform_counts.index, lifeform_counts.values)]
plt.legend(wedges, legend_labels, title='Жизненная форма: Количество', 
              loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.show()

# Приступим к написанию функции search_plants(), которая создает консольное приложения для выбора
# комбинации почва-свет-влага с последующим выводом пользователю списка растений, соответствующего
# выбранной комбинации. 
# Сперва сохраняем в переменные уникальные типы почвы, света и влаги.

def search_plants():
    print("\n=== Поиск растений по параметрам ===")
    
    soils_unique = sorted(df['Почва'].unique())
    lights_unique = sorted(df['Свет'].unique())
    moistures_unique = sorted(df['Влага'].unique())

# После этого предлагаем пользователю выбрать один из уникальных типов почвы, либо «Не задано»,
# если этот критерий нужно пропустить. Выбранный пункт сохраняем в selected_soil.

    print("\nВыберите тип почвы:")
    for i, soil in enumerate(soils_unique, 1):
        print(f"{i}. {soil}")
    print(f"{len(soils_unique) + 1}. Не задано")
    
    soil_choice = int(input("Введите номер: "))
    if soil_choice == len(soils_unique) + 1:
        selected_soil = None
    else:
        selected_soil = soils_unique[soil_choice - 1]

# По аналогии с выбором типа почвы предлагаем пользователю выбрать свет и влагу. Сохраняем выбор в
# переменные selected_light и selected_moisture соответственно.

    print("\nВыберите тип света:")
    for i, light in enumerate(lights_unique, 1):
        print(f"{i}. {light}")
    print(f"{len(lights_unique) + 1}. Не задано")
    
    light_choice = int(input("Введите номер: "))
    if light_choice == len(lights_unique) + 1:
        selected_light = None
    else:
        selected_light = lights_unique[light_choice - 1]
    
    print("\nВыберите тип влаги:")
    for i, moisture in enumerate(moistures_unique, 1):
        print(f"{i}. {moisture}")
    print(f"{len(moistures_unique) + 1}. Не задано")
    
    moisture_choice = int(input("Введите номер: "))
    if moisture_choice == len(moistures_unique) + 1:
        selected_moisture = None
    else:
        selected_moisture = moistures_unique[moisture_choice - 1]

# Теперь нужно отсортировать растения по выбранной комбинации. Для начала создаем массивы plants,
# lifeforms, soils, lights и moistures, которые соответствуют столбцам нашего датасета. С помощью
# функции np.where() получаем массив индексов всех строк, которые подходят под выбранную комбинацию.
# С его помощью отделяем filtered_plants и filtered_lifeforms из массивов всех растений и всех
# жизненных форм соответственно.
# Выводим пользователю результаты поиска: почву, свет и влагу, которые он выбрал, количество
# найденных растений и их список. 

    plants = df['Название растения'].values
    lifeforms = df['Жизненная форма'].values
    soils = df['Почва'].values
    lights = df['Свет'].values
    moistures = df['Влага'].values
    
    indexes = np.where(
        (soils == selected_soil if selected_soil else True) &
        (lights == selected_light if selected_light else True) &
        (moistures == selected_moisture if selected_moisture else True)
    )[0]
    
    filtered_plants = plants[indexes]
    filtered_lifeforms = lifeforms[indexes]
    
    # Вывод результатов
    print("\n=== Результаты поиска ===")
    print(f"Почва: {selected_soil if selected_soil else 'Не задано'}")
    print(f"Свет: {selected_light if selected_light else 'Не задано'}")
    print(f"Влага: {selected_moisture if selected_moisture else 'Не задано'}")
    print(f"Найдено растений: {len(filtered_plants)}\n")
    
    for plant, lifeform in zip(filtered_plants, filtered_lifeforms):
        print(f"{plant} - {lifeform}")

search_plants()
