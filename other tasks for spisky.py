
# Напишите программу на Python для удаления дубликатов из списка
#
# не оч.понял что за дубликат но тем не менее
#
# Alexey: дубликат это не уникальный элемент, которыми в этом списке являются 2, 3, 4
# тк они повторяются поэтому все вхождения больше одного раза отсекаются
#
# a = [2,3,4,5,2,3,4]
# y = list(set(a))
# print(y)
#
# a = [2,3,4,5,2,3,4,2,3,2,2,2]
# y = a.count(2)
# print(y)

# все понятно

# Напишите программу на Python,
# чтобы проверить, пустой список или нет.
#
#
# a = [2,3,4,5,6,7,8,9,10]
# e = len(a)
# print(e)

# миллион команд через которые можно проверить длинуспик
#
# сама же длина через иф я только увидел как определяется
#


# Напишите программу на Python для клонирования или копирования списка
#
# a = [3,4,6,1,2,6,7,8]
# y = a.copy()
# print(y)
# понятно все


# Напишите программу на Python, чтобы найти список слов, длина которых превышает n, из заданного списка слов
#
# a = ['dkasbvsjnv','verder','psv','leeds','hfbfhdbk']
# s = max(a,key=len)   # с ключом выдает самое длинное слово
# n = min(a)          # выдаедает самое длинное а не короткое слово
# print(s,n)
#


# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
#
# a = [1,1]
# b = a.insert(1,0000000000000000000000000000000000000000) 
# print(a)

# ПОЧЕМУ ОН НЕ ПОКАЗЫВАЕТ ТО ЧТО НУЖНО ВСЕ ПРАВИЛЬНО И МЕТОД И СИНТАКИСИС А ОТВЕТ 0 а не 100 0

# Alexey: потому что 00000 = 0 , а вот 0, 0, 0 = 0, 0, 0
# В первом случае сколько раз 0 в одну строку не пиши на деле это один 0
# а если его писать через запятую то их несколько,
# но для решения программы тебе нужен цикл


#
# a = [1,1]
# b = a.extend([00000000000000000000000000000000000000000000000000000000000000000000000000000000])
# print(a)

# вот две команды все выполняны две команды выполнены правильно , в данном моменте адекватна первая команда



# Сформировать возрастающий список из чётных чисел (количество элементов 45)

# a = [2,4,6,8,10,12,14,16,18,20]
# c = a.sort(0,14)# чо за хрень с синтакисимом
# print(a)

# единственное адекватное команада увеличивающаяся список это сорт (косвенный метод)
# но я вижу увиличения через списковое включение

# a = [2,4,6,8,10,12,14,16,18,20]
# b = [i*2 for i in a]
# print(b)

# идеально двойной цикл увеличивает вводные из списка
# Alexey: ты если не совсем понимаешь задачу лучше у меня спрашивай, тк здесь имелось ввиду создать
# списко идущий по возрастанию и состоящий из четных элементов и количество этих элементов должно быть 45
# а на деле у тебя это 45 никак не учавствует в задаче вообще ты опять придумал свои условия
#

#
# Пользователь вводит число. Определить, содержит ли список данное число x.
# Если содержит, то вывести на экран число 7145,
# если не содержит,
# то вывести на экран число 5741;

# c = int(input())
# a = [2,4,6,8]
# b = a.index(0,-1)
#     if c == 4:
#         print(a,b)
# else:c != 4
# print(5741)

# в чом проблема синтаксиа  метода иф елсе в нем проблема но все же правильно
# Alexey: это лучше разберем на созвоне, если и исправить ошибку синаксиса if..else задача все равно делает ерунду

# я просто немного расфокусировался



# сумму всех чисел списками
#
# f = [2,4,6,8]
# y = sum(f)
# print(y)

# все ок

# Найти наибольший элемент списка и вывести его на экран
#
# g = [85,949,1,245,19393,234,12,34]
# d = max(g)
# print(d)

# выполнено