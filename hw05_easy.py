# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_path = []

for i in range (9):
    dirr = "dir_" + str(i+1)
    dir_path.append (os.path.join(os.getcwd(), dirr))
    print (dir_path [i])
try:
    for i in range (9):
        os.mkdir(dir_path[i])
except FileExistsError:
    print('Такая директория уже существует')

try:
    for i in range (9):
        if os.path.exists (dir_path[i]):
            os.rmdir (dir_path[i])
except FileNotFoundError:
    print('Такая директория не существует')
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print (os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

file_name = str (__file__)

try:
    shutil.copy (file_name, 'my_copy.py')
except FileExistsError:
    print('Такой файл существует')
