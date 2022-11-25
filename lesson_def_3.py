"""
Функции в которые получаешь:
- названия чая,
- ингридиенты бутерброда,
- достаешь шоколадку по названию
и финальная функция съесть все
"""


def eat(tea, doner, schokolate):
    tea_in_cup = make_tea(tea)
    burger_in_table = make_burger(doner)
    schokolate_in_hand = get_schokolate(schokolate)
    text_of_dinner = tea_in_cup + '\n' + burger_in_table + '\n' + schokolate_in_hand + '\n'
    return text_охуеть
    of_dinner + 'very yammi'

def make_tea(name_tea):
    return 'Выпит отличный чай который называется ' + name_tea + '. '

def make_burger(ing):
    return 'Cъеден отличный бутерброд c ' + ing + '. '

def get_schokolate(name):
    return 'Хорошая шоколадка была ' + name + '. '

# res_trapesa = eat(input('input tea: '), input('input doner: '), input('input chk: '))
# print(res_trapesa)
print(make_burger(input('input doner: ')), make_burger(input('input doner: ')),)


