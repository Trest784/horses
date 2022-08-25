
#цвета клубов
R = "red"
W = 'white'
B = 'blue'
BLC = 'black'
G = 'green'
P = 'pink'
Y = 'yellow'


def colors_clubs():
    milan = milan_colors
    nant = nant_colors
    sevilla = sevilla_colors
    rangers = rangers_colors
    return milan, nant, sevilla, rangers


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

print(milan,nant,sevilla,rangers)
colors_clubs()

#час сижу не могу решение найти он мне просто сейчас выдает что где лежит и все не какого толку

# по сколько я не понял причину ошибки и почему он выдает что просто что то сидит в ячейки
# я попробую сделать такую же элементарную задачу


#

a = 'voda'
b = 'v'
c = 'stakane'
d = 'stoyt na stole'

def aqua(rom, cola):
    rom = posuda(a, b, c)
    cola = kuhnya(a, b, c, d)
    return rom, cola


def posuda(a, b, c):
    posuda = a+b+c
    return posuda


def kuhnya(a, b, c, d):
    kuhnya = a+b+c+d
    return kuhnya


print(aqua(rom, cola))

# я не понимаю в чем ошибка ебанный в рот
# у каждой переменной есть свои аргументы, в чем ебучая проблема почему так