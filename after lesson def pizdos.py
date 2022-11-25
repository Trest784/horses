 # вытащить ключи и значения из словарей
 # превратить их в список
 # и получить общее количество символов в списке


alf_dict = {"sevilla":"emery","monaco":"henry","MU":"cr7"}
bas_dict = {"KFC":"chicken","oneill":"beers","MCD":"hamburger"}

# def say_hello(name):
#     print('Hello, ' + name)
#
# var_name = 'Alexey'
# # say_hello('Andrey')
# # say_hello(var_name)
# say_hello('rogozin1')
# b = 'rogozin2'
# say_hello(b)
# say_hello(var_name)


def combiantion9(dict1, dict2):
    combs1 = keys_in_list(dict1.keys(), dict2.keys())
    combs2 = values_reversed(dict1.values(), dict2.values())
    combs3 = result(combs1, combs2)
    sum_combs = combs1 + combs2
    combs4 = kolichestvo(sum_combs)
    return sum_combs, combs4


def keys_in_list(keys1, keys2):
    return list(keys1), list(keys2)


def values_reversed(value1, value2):
    return list(value1)[::-1], list(value2)[::-1]


def result(bar1, bar2):
    return list(bar1), list(bar2)


def kolichestvo(qwa1):
    return len(qwa1)


itog = combiantion9(alf_dict, bas_dict)
# print(itog)


# x = int(input('enter'))
list_val = list(range(101))


def mult3(y):
    return y * 3


for el in range(len(list_val)):
    x = list_val[el]
    print(mult3(x))

# print(mult3(x))

