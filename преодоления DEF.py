
"Напишите программу на Python для обращения строки."
"Пример строки : «1234abcd»"
"Ожидаемый результат : dcba4321"

# var1



alt = "1234abcd"


def reverse(suit):
    suit = reversed_alt = alt[::-1]
    return suit


#print(reverse(alt))


#

# var2

alt = "1234abcd"


def reverse(suit):
    bong = reversed_suit = suit[::-1]
    return bong


# print(reverse(alt))

# оба варианта рабочии, оба варианта дают правильный ответ у них одна и та же инструкция
# НО КАКОЙ ВАРИАНТ БОЛЕЕ ОПТИМАЛЕН С ТОЧКИ ЗРЕНИЯ РАБОТЫ С ПЕРЕМЕННЫМИ??


# Напишите функцию Python для вычисления факториала числа

# N = int(input("Enter the number"))
#
#
# def factorial(ss):
#     if ss == 0:
#         return 1
#     else:
#         return ss * factorial(ss - 1)


# print(factorial(N))


# Напишите функцию Python, чтобы проверить, находится ли число в заданном диапазоне

lenta_list = [23,11,123,77,88,100,7,777,7777,7]


def search(int):
    bar = int.count(7)
    return bar


# print(search(lenta_list))



# соеденить два списка,
# добавить к нему значения любое



# nesta_list = ['milan', 'messi', 'pirlo', 'barca', 'dzaneti']
# # int_list = [333, 11, 45, 789, 23, 32, 2332, 1]
# #
# #
# #
# #
# #
# # def definit(ert,tre):
# #     asa = sum_list(ert, tre)
# #     sas = king_list(asa)
# #     return sas
# #
# # def sum_list(bld, bls):
# #     doom_list = bld + bls
# #     return doom_list
# #
# # def king_list(ala):
# #     # parma_list = ala.append(['burgers'])
# #     # return parma_list
# #     ala.append(['burgers'])
# #     return ala
# #
# #
# # print(definit(nesta_list, int_list))



nesta_list = ['milan', 'messi', 'pirlo', 'barca', 'dzaneti']
int_list = [333, 11, 45, 789, 23, 32, 2332, 1]
baban_list = ['burgers']





def definit(ert,tre,dfr):
    asa = sum_list(ert, tre)
    sas = king_list(dfr, asa)
    show_king_list(sas[-1])
    sera = reverse_banan(dfr)
    triziny = favorites(ert)
    mini = tika(tre)
    # luda = badanov(triziny,mini)
    return sas,sera,triziny,mini,

def sum_list(bld, bls):
    doom_list = bld + bls
    return doom_list

def king_list(dfr,ala):
    ala.append(dfr)
    return ala

def show_king_list(var1):
    print(var1[0][0])


def reverse_banan(dfr):
    dora = reversed(dfr[::-1])
    return dora

def favorites(ert):
    stroomzy = ert[1:4]
    return stroomzy


def tika(tre):
    soka = tre[-1]
    lara = str[soka]
    return lara


# def badanov(triziny,mini):
#     kaka = triziny + mini
#     return kaka





print(definit(nesta_list, int_list, baban_list))




