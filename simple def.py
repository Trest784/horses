car = 100
moto = 10

def supercar():
    dj = car + moto
    return dj

supercar()
print(supercar())

# так она дает ответ 110
#
# но если мы введем аргументы у супер мото примует ли они их

# car = 100
# moto = 10
#
# def supercar(dj,mc):
#     dj = car + moto
#     mc = car - moto
#     return dj,mc
#
# supercar(car,moto)
# print(supercar(dj,mc))

# вот почему они не работают почему, ведь 23 строчка говорит 18 какие аргументы принять в переменные
# и с каими данными из глабала работать и дж и мс но они с ними не работают
# я вот этого вообще не понимаю

# попробуем так

car = 100
moto = 10


# def supercar():
#     dj = car + moto
#     mc = car - moto
#     print(dj, mc)
#     return dj, mc
#
#
# print(supercar())



# так он тоже не принимает переменные непонятно
# car = 100
# moto = 10
#
# def supercar(dj,mc):
#     global car,moto
#     dj = car + moto
#     mc = car - moto
#     return dj,mc
#
# supercar(car,moto)
# print(supercar(dj,mc))

# и так нет но почему