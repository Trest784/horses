
# Напишите функцию dislike_6(a), которая всегда возвращает True,
# если только не передается число 6 типа int или типа float (в данном случае она вернет «Только не 6!»).

a = int(input("enter the number"))

def dislike_6(a):
    if a == 6:
        print('true')
    else: a != 6
    print('false')

def dislike_6():

# вот что не так ? ошибка отступа он говорит но где она он говорит о 13 строке но там же все ок??

#вот их решения:

# def dislike_6(a):
#     if (type(a) is float or type(a) is int) and a == 6.0:
#         return 'Только не 6!'
#     return True


# Тесты
# print(dislike_6(6.0))
# print(dislike_6(6))
# print(dislike_6('6'))
# print(dislike_6('Хорошо'))
# print(dislike_6([6, 6]))


# чем их решение лучше чем мое, по моемо не особо то их решение крутое









# После
# изучения
# темы «Логический
# тип
# в
# Python» перед
# учеником
# стала
# задача
# написать
# функцию
# divider(a, b), принимающую
# любые
# 2
# числовых
# параметра.
# Задача
# функции: разделить
# a
# на
# b.
# Если
# в
# знаменателе
# введут
# ноль, то
# результат
# будет
# следующим: «Нули
# в
# знаменателе
# не
# приветствуются».
# В
# противном
# случае
# выводится
# итог
# деления
# чисел, возведенный
# в
# куб.
# Решите
# задание
# без
# использования
# условия if, применяя
# свойства
# логических
# операторов.

a,b = int(input('a =')),int(input('b ='))   #здесь же нет не правильного отступа а он говорит что есть

def  divider(a,b):
    sum_num = a + b
    if sum_num != 0:
        print("true")
    else: sum_num == 0
    print("false")


def  divider(a,b):




# опять ошибка отступа, в чем дело?


# их решение
# def divider(a, b):
#     return b and (a / b) ** 3 or 'Нули в знаменателе не приветствуются'
#
#
# print(divider(10, 4))
# print(divider(10, 0))
# print(divider(-12.2, 2))
# print(divider(-6.4, 0))

# чо за шляпа, почему у них такое решение и что она дает





# Дано 2 скрипта. В первом – возникает ошибка, во втором – ошибки нет.
# Поясните почему.
#
# Скрипт 1.
a = None
  if len(a) > 0 and a is not None:    думаю что здесь ошибка синтакисиа так как условие а не равно none это условие которое
      print('OK')                          подходит под условие иф и оно должно стоять первым
#
# Скрипт 2.
a = None
if a is not None and len(a) > 0:
    print('OK')


# Напишите функцию Python,
# которая берет список и возвращает новый список с уникальными элементами первого списка

list_diapazon = [1,1,1,3,3,3,55,55,67,67,100,100,22,22]


# def diapazon(list_diapazon):
#     for i in list_diapazon:
#         i = append(list_diapazon)
#         print(i)
#
#
# def diapazon():


# Напишите функцию Python,
# которая принимает строку и рассчитывает количество букв верхнего и нижнего регистра

fraza = "welcome to barcelona"


def citata(fraza):
    b = len_fraza(fraza)
    print(b)


def citata(fraza):


# их решение

# def unique_list(l):
#     x = []                 не могу понять сути этой строчки 
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
#
#
# print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))