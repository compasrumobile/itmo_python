# -*- coding: utf-8 -*-
import os
a = '.'
"""
# Вариант с вводом пути пользователем
a = input('Введите путь к папке (с двумя обратными слэшами):\n')
"""
if not os.path.exists(a): # Checking for folder existance
    print('Путь указан некорректно')
else:
    b = os.listdir(a)
    x = 0

    for item in b:
        
        if os.path.isfile(item):
            g = open(item, 'r', encoding='utf-8').read() #Как присвоить g путь файла?
            
            if 'python' in g:
                print(item)
                open('result.txt', 'a', encoding='utf-8').write(item+'\n')
                x += g.count('python')
    print(x)
    open('result.txt', 'a', encoding='utf-8').write(str(x))
