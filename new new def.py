

crabs_list = [2, 3,4,5,6,7]
souse_list = [10,11,12,23]


def tarelka(mix_list, banan):
    yammi = list_extend(banan)
    food = my_reverse(mix_list)
    shielding(food)
    return yammi, food


def list_extend(banan_souse):
    """Смешивает листы"""
    crabs_list.extend(banan_souse)
    return crabs_list

def my_reverse(mix_crab_list):
    """Переворачивает листы"""
    nice_kitchen_list = mix_crab_list[::-1]
    return nice_kitchen_list

def shielding(knife):
    """Экранирует листы"""
    for i in knife:
        print(i)

# print(mix_list, nice.kitchen_list, i)
# print(tarelka(crabs_list, souse_list))

x = [1,2,3,3,4,5,6,7,7,8,9,0,0,21,2,]
# shielding(x)



# в чем проблема не ушто взята не правильно аргументы в параметры???
# по легбу же он должен же был принять аргументы в 6 строку из 3 и 4 без никаких проблем абсолютно



foods_dict = {'burger':'cola','potato':'souse','icecream':'chocolate'}


def yammi(fd):
    foods = list(fd.keys())
    additionaly = list(fd.values())
    return additionaly,foods


print(yammi(foods_dict))


# ЧТО НЕ ТАК?


dil = ['barca']
liv = ['liver']


def champ(brc):
    brc.append('champion')
    return brc


print(champ(dil))

# print(champ(dil))
# print(champ(liv))
# print(champ(['inter']))


