# -*- coding: utf-8 -*-
import os

#a = input('Введите путь к папке (с двумя обратными слэшами):\n') # вариант, когда путь вводит пользователь
a = 'D:\\Google\\Python\\Courses\\Lesson2'

if not os.path.exists(a): # Checking for folder existance
    print('Путь указан некорректно')
else:
    b = os.listdir(a) 
    x = 0
    for item in b:
        c = (os.path.join(a, item)) # присвоение переменной абсолютного пути текущего файла или папки 
        if os.path.isfile(c): # проверка, явлется ли item файлом
            g = open(c, 'r', encoding='utf-8').read() # открытие на чтение  
            if 'python' in g: # есть ли в содержимом файла "python"?
                print(item)
                open(os.path.join(a,'result.txt'), 'a', encoding='utf-8').write(item+'\n') # записать в result.txt имя файла, содержащего "python"
                x += g.count('python') # счетчик файлов, содержащих "python"
    print(x)
    open(os.path.join(a,'result.txt'), 'a', encoding='utf-8').write(str(x))
