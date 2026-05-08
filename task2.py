#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Импортируем модуль sys для взаимодействия с командной строкой.
import sys


# In[11]:


# Считываем координаты центра эллипса и длину его радиусов из txt-файла.
def read_ellipse_file(file_path):
    with open(file_path, 'r') as f:
        center_x, center_y = map(float, f.readline().strip().split())
        radius_a, radius_b = map(float, f.readline().strip().split())
    return center_x, center_y, radius_a, radius_b


# In[12]:


# Из другого файла последовательно считываем строки, каждая из которых содержит координаты произвольной точки.
# Объединяем пары координат в один список.
def read_points_file(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


# In[13]:


# Определяем полоджение точек относительно эллипса.
def point_position(point, center, radius_a, radius_b):
    # Выполняем распаковку кортежей, содержащих координаты центра и точек.
    x, y = point
    center_x, center_y = center
    
    # Вычисляем относительные координтаы точек.
    x_rel = (x - center_x) / radius_a
    y_rel = (y - center_y) / radius_b
    
    # Решаем уравнение эллипса.
    ellipse_equation = x_rel**2 + y_rel**2
    if ellipse_equation_value < 1:
        return 1  # Точка находится внутри эллипса.
    elif ellipse_equation_value > 1:
        return 2  # Точка находится снаружи эллипса.
    else:
        return 0  # Точка лежит на эллипсе.


# In[14]:


# # Адаптируем функции для работы с командной строкой.
# Проверяем, что в командной строке переданы все необхожимые аргументы: название скрипта, а также пути к обоим файлам.
def main(args):
    if len(args) != 3:
        print("Использовать: python script.py ellipse_file points_file")
        return
        
# Для дальнейшей работы сохраним пути к файлам в отдельные переменные.    
    ellipse_file = args[1]
    points_file = args[2]

# Считываем необходимые числа из файлов.
    center_x, center_y, radius_a, radius_b = read_ellipse_file(ellipse_file)
    points = read_points_file(points_file)

# Сохраним координаты центра эллипса в отдельную переменную.
    center = (center_x, center_y)

# Определяем положения точек относительно эллипса.
    for point in points:
        position = point_position(point, center, radius_a, radius_b)
        print(position)
        
# Завершаем работу с командной строкой.
if __name__ == "__main__":
    main(sys.argv)


# In[ ]:





# In[ ]:




