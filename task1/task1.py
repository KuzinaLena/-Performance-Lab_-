#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Импортируем модуль sys для взаимодействия с командной строкой.
import sys


# In[2]:


# Создаём функцию для генерации кругового массива (массива из n чисел от 1 до n).
def generate_circular_array(n):
    return list(range(1, n + 1))


# In[4]:


# Создаём функцию для вывода пути по круговому массиву в зависимости от интервала m.
def get_path(circular_array, m):
    path = []
    start_index = 0
    # Сохраним длину исходного массива в отдельную переменную.
    length = len(circular_array)

    while True:
        # Вычисляем индекс последнего элемента интервала.
        end_index = (start_index + m - 1) % length
        # Добавляем в список индекс первого элемента в первом интервале.
        path.append(circular_array[start_index])
        # Обновляем значение индекса, с которого начинается следующий интервал.
        start_index = end_index
        
        # Программа досрочно завершается, если во время обхода снова возвращается к элементу массива с индексом 0.
        if start_index == 0:
            break
# Преобразуем список индексов в единую строку символов.
    return ''.join(map(str, path))


# In[6]:


# Адаптируем функции для работы с 2 массивами одновременно.
# Проверяем, что в командной строке переданы все необхожимые аргументы: название скрипта, а также параметры n и m для каждого из массивов.
def main(args):
    if len(args) != 4:
        print("Использовать: python script.py n1 m1 n2 m2")
        return
    # Считываем значения n и m для обоих массивов из аргументов командной строки.
    n1, m1 = int(args[1]), int(args[2])
    n2, m2 = int(args[3]), int(args[4])
    
    # Генерируем 2 круговых массива заданной длины.
    circular_array_1 = generate_circular_array(n1)
    circular_array_2 = generate_circular_array(n2)

    # Получаем путь для обоих массивов.
    path1 = get_path(circular_array_1, m1)
    path2 = get_path(circular_array_2, m2)

    # Объединяем пути для обоих массивов в одну строку.
    result = path1 + path2
    print(result)
    
# Завершаем работу с командной строкой.
if __name__ == "__main__":
    main(sys.argv)


# In[ ]:




