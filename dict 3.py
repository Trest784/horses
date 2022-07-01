
# вложенный словарь

clubs = {}
clubs['sevilla'] = {'navas','silva'}
clubs['atletico'] = {'karasco','savic'}
print(clubs)

#cуть понятна

# посмотрел еще другие способы этот как мне кажется самый быстрый и оптимальный
#







# объединения словарей (двойной словарь)

sevilla = {'navas','silva'}
atletico = {'karasco','savic'}
fc = sevilla|atletico
# print(fc)

# как работает понятно
# НО НЕПОНЯТНО следующие
# вот что
# вот ответ - {'savic', 'navas', 'karasco', 'silva'}
# по синтаксису получается что да,НО по смсылу нет
# нет пары ключ значения , есть список в форме  словаря

# вот лучший способ на мой взгляд

a = {'d': 23,'h': 77}
a.update(c = 67, n = 77)
# print(a)
# a = 'asd'
# [print(x, end=', ') for x in dir(a) if not x.startswith('__')]
# почему NONE


def my_update(arg):
    arg.popitem()
    arg.update(a=67, b=77)
    arg.popitem()
    arg.update(a=67, b=77)
    arg.popitem()
    arg.update(a=67, b=77)
    return arg


b = {1: 'asd'}
a = my_update(b)
x = my_update(a)
a = my_update(b)
x = my_update(a)
a = my_update(b)
x = my_update(a)
a.popitem()
a.update(a=67, b=77)
b.popitem()
b.update(a=67, b=77)
# print(a)

# print(sum([1, 3]))

a = {'a':1,'b':2,'c':3}
# f = a.get('a')
# g = a.get('c')
# print(sum([f,g]))

res = a.get('a') + a.get('c')
res2 = 1 + 2
# print(res)

# print(sum(a.values()))

d = a.get('a') / a.get('b')
a.update({'c': d})
# print(a)

f = a.keys()
# print(f)
temp = ''

for x in f:
    temp += x
    # print(x, end="")

# print(temp)
x = ''.join(('ya', 'vldm', 'vlamrch'))
print(x)
# split
