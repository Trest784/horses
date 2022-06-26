
#GET

# метод get() вовзращает значение по указанному ключу.
# Если указанного ключа не существует то он вернет метод none

a = {'euro_food': 'pizza','uzbek-food':'cheburek','japan-food':'sushi'}
b = a.get('japan-food')
print(b)

y = {'espana':'FCB','apl':'leeds united','holland':'feinord'}
n = y.get('espana')
print(n)

c = {'0':0,'1':1,'2':2}
m = c.get('1')
print(m)

yuo = {'1':'NWA','first1':'108','3':'ug'}
p = yuo.get('3')
f = yuo.get('first1')
print(p,f)

fcb = {'messi':1,'inesta':10,10:'xavi'}
s = fcb.get(10,'inesta') #почему инеста не выдает свою 10ку
print(s)



# ITEMS

# Команда items() возвращает объект представления,
# который отображает список пар кортежей словаря (ключ, значение).

q = {'f': 1,'w': 2,'e': 3}
w = q.items()
print(w)


# # я хотел вывести значение одного ключа
# e = {'f': 1,'w': 2,'e': 3}
# w = e(f) #почему не работает через () и не работает через []
# print(w)
# # почему нет
# # только целый словарь он превращает в кортеж???

dictionary = {'f': 1,'w': 2,'e': 3}
s = dictionary.items()
print(s)
# реально как я понимаю items дает только одно значения


#values

# Метод values() возвращает объект представления,
# который отображает список всех значений в словаре.
# выдает значения по ключу

s = {'laliga': 1,"lique": 'only_marselee'}
a = s.values()
print(a)

e = {'laliga': 1,"lique": 'only_marselee'}
a = e.values() # вводил ла лига что бы он вернул один аргумент но он выводит только значения в словаре целиком
print(a)
