import os
import time
from random import randint
# Основное меню (болванка)
'''print('Привет! Выбери, что ты будешь делать первым делом')
print('')
print('1. Проверка таблицы умножения')
print('2. Проверка деления')
userChoise = int(input())
while True:
    if userChoise != 1 and userChoise != 2:
        os.system('cls')
        print('Нажми [1] и [Enter] для проверки таблицы умножения или [2] и [Enter] для проверки деления!')
        print()
        print('1. Проверка таблицы умножения')
        print('2. Проверка деления')
        userChoise = int(input())
    else:
        break'''
# Проверка таблицы умножения
print('Реши правильно 20 примеров.')
print()
import datetime
errCount = 0
startTime = datetime.datetime.now()
for k in range(20):
    a = randint(2,5)
    b = randint(2,9)
    rightOtvet = a * b
# Меняем аргументы местами
    while True:
        if (k + 1) % 2 != 0:
            print(k + 1, ') ', a, ' x ', b, ' = ', sep='', end='')
        else:
            print(k + 1, ') ', b, ' x ', a, ' = ', sep='', end='')
        userOtvet = int(input())
        if userOtvet == rightOtvet:
            print('Правильно!')
            print()
            break
        else:
            errCount = errCount + 1
            print('Неправильно, попробуй еще раз!')
            print()
endTime = datetime.datetime.now()
delta = endTime - startTime
prError = round(errCount / 20 * 100)
verno = 100 - prError
if errCount == 1 or errCount == 21:
    errWord = 'ошибка.'
elif 2 <= errCount <= 4 or 22 <= errCount <= 24:
    errWord = 'ошибки.'
else:
    errWord = 'ошибок.'
print('Секундочку....')
time.sleep(1)
os.system('cls')
print('Молодец, ты справился!')
while True:
    if errCount != 0:
        print('Но у тебя', errCount, errWord)
        print('В следующий раз будь внимательнее и у тебя всё получится!')
        break
    else:
        print('Ты решил всё правильно! Без единой ошибки! Так держать!')
        break
print()
# Запись статистики в файл
today = datetime.datetime.today()
os.chdir('D:\Mike')
f = open('results.txt', 'a')
f.write(today.strftime("%d/%m/%Y - "))
f.write(time.strftime("%H:%M:%S"))
f.write('\n')
f.write('Затрачено времени: ')
f.write(str(delta))
f.write('\n')
f.write('Количество ошибок: ')
f.write(str(errCount))
f.write('\n')
f.write('Количество правильных ответов:')
f.write(str(verno))
f.write('%')
f.write('\n')
f.write('-----')
f.write('\n')
# f.write('Ошибки:')
f.write('\n')
f.close()
input('Для выхода нажми клавишу ENTER')
