# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

string = ["яблоко", "банан", "киви", "арбуз"]

x = 0
for i in string:
    x = x + 1
    print(x,".", '{:>10}'.format(i))
	
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

string1 = ["яблоко", "банан", "киви", "арбуз"]
string2 = ["яблоко", "арбуз"]

result = list(set (string1) - set (string2))
print (result)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [1, 5, 16, 17, 27, 28, 31, 45, 59, 63, 64, 67, 68, 69, 70, 75, 76, 77, 78, 79, 83, 86, 89, 98, 99]

new_numbers = [0] * len(numbers)

x = 0

for i in numbers:
    if i % 2 == 0:
        new_numbers [x] = i / 4
    else:
        new_numbers [x] = i * 2
    x = x + 1

print (new_numbers)

