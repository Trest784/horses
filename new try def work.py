
#цвета клубов
R = "red"
W = 'white'
B = 'blue'
BLC = 'black'
G = 'green'
P = 'pink'
Y = 'yellow'

def colors_clubs(clr1, clr2, clr3, clr4, clr5, clr6, clr7):
    milan_res = milan(clr1, clr2)
    nant_res = nant(clr5, clr7)
    sevilla_res = sevilla(clr1, clr3)
    rangers_res = rangers(clr4, clr3)
    palermo = clr6 + clr2
    return milan_res, nant_res, sevilla_res, rangers_res, palermo


def milan(R,BLC):
    milan_colors = R + BLC
    return milan_colors


def nant(G,Y):
    nant_colors = G + Y
    return nant_colors


def sevilla(R,W):
    sevilla_colors = R + W
    return sevilla_colors


def rangers(B,W):
    rangers_colors = B + W
    return rangers_colors





print(colors_clubs(R, BLC, W, B, G, P, Y))

#час сижу не могу решение найти он мне просто сейчас выдает что где лежит и все не какого толку

# по сколько я не понял причину ошибки и почему он выдает что просто что то сидит в ячейки
# я попробую сделать такую же элементарную задачу


#

a = 'voda'
b = 'v'
c = 'stakane'
d = 'stoyt na stole'

def aqua(arg1, arg2, arg3, arg4):
    rom = posuda(a, b, c)
    cola = kuhnya(a, b, c, d)
    return rom, cola


def posuda(a, b, c):
    posuda = a+b+c
    return posuda


def kuhnya(a, b, c, d):
    kuhnya = a+b+c+d
    return kuhnya


# print(aqua(a, b, c, d))

# я не понимаю в чем ошибка ебанный в рот
# у каждой переменной есть свои аргументы, в чем ебучая проблема почему так