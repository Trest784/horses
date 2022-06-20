
#1 вырезать первые пять данных

list_a = [2,3,4,5,6,7,8,9,1,2,6,72,432,535,46,76,68,34]
list_ab = slice(6) # Alexey: почему не list_a[:5]?
# print(list_a[list_ab])

#nice

#2 все четные до 6

list_b = [0,1,2,3,4,5,6,7,8,9,10]
x = slice(0,6,2) # Alexey: list_b[0:7:2]
# print(list_b[x])

#3 несколько элементов из нескольких списков
#
list_b = [0,1,2,3,4,5,6,7,[23,23,3,44,56,77,12]]
# x[0] = slice(1,4)
x = list_b[:3]
# y[1] = slice(2)
# y = slice(2)
# print(x)

# заебало что с синтаксисом почему такая проблема с синтаксисиом у слайсинга с двойным списком

#4

# list_b = ["nevill","denisov","raul"]
# list_b[0] = slice(3)
# list_b[1] = slice(4)
# list_b[2] = slice(0)
# print(list_b[0,1,2])

list_b = ["nevill","denisov","raul"]
y = list_b[0][0]
c = list_b[1][0]
e = list_b[2][0]
# print(y,c,e)

#  БЛЯ ДОПЕР ДО СИНТАКИСИА ВСЕ - ОЧЕНЬ ДОЛГО ЩАС КОВЫРЯЛСЯ ПИЗДОС

# 5
# ТАКЖЕ ЧТО НИБУДЬ РАЗДРОБЛЮ
list_c = ['bremen','union','inter',]
b = list_c[0][-1]
u = list_c[1][-1]
i = list_c[2][2:]
# print(b,u,i)

# list_index

list_b = [2,3,4,5,6,7,8,9,10,12,3,3,5435646,2423,76578,1]
index = list_b.index(2,0,3)
# print(index)


list_v = [6,5,4,3,2,6,7,89,0,123,343,46578,68,90,34,4,00,998,7,65,44,33,21]
index = list_v.index(33)
index1 = list_v.index(2)
# print(index,index1)

#
#
#
#
