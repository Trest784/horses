# Напишите функцию Python для суммирования всех чисел в списке
# Список образцов : (8, 2, 3, 0, 7)

# мое решение

int = 8
bad = 2
rat = 3
sad = 0
dsd = 7


def sum():
    sum = int + bad + rat + sad + dsd
    return sum


print(sum())

# правда здесь нет переменных у sum

# попробую тоже самое но с переменными:

int = 8
bad = 2
rat = 3
sad = 0
dsd = 7


def sum(ddd,qqq,eee,ttt,uuu):
    sum = ddd + qqq + eee + ttt + uuu
    return sum


print(sum(int,bad,rat,sad,dsd))

# так работает ,а если так:

# int = 8
# bad = 2
# rat = 3
# sad = 0
# dsd = 7
#
#
# def sum(op):
#     op = int + bad + rat + sad + dsd
#     return op
#
#
#
# print(sum(op))


# задача 2 (в задачнике 3)

# Напишите функцию Python для умножения всех чисел в списке
# (8, 2, 3, -1, 7)

asap_list = [8, 2, 3, -1, 7]

def wasp(ye):
    for i in asap_list:
        result = i * 1
        return result


print(wasp(asap_list))

# так он дает 8 но почему и что это и как почему 8 блять

asap_list = [8, 2, 3, -1, 7]

def wasp(ye):
    wasp_list = [i * 5 for i in asap_list]
    return wasp_list


print(wasp(asap_list))

# бля с точки зрения функций все сделано правильно , с точки зрения умножения списка нет так как я все позиции на 5 умножил а не конкретно
# каждую позицию друг на друга

# решения из решебника (так как я типо все правильно сделал с точки зрения функции то смотрю по математике)

# их решения
#
# 1	def multiply(numbers):
# 2	    total = 1
# 3	    for x in numbers:
# 4	        total *= x
# 5	    return total
# 6	print(multiply((8, 2, 3, -1, 7)))

# по какой хуй нужна строчка 2 (90) не понимаю
