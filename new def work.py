# по стараюсь на базе проработанного что то сделать

afk_list = [22,22,33,45,33,1,2,8,6,77,77]


def function(baza):
    a = [i*2 for i in baza]
    return a


b = function(afk_list)
print(b[1:3])

# по содержанию бред, но весь синтаксис и логика сделаны правильно как я понимаю?
# попробую сделать





afk_list = [22,22,33,45,33,1,2,8,6,77,77]


def function(afk_list):
    a = [i*2 for i in afk_list]
    print(a)
    return a

# x = function(afk_list)


# то же самое,но более лаконично и более коротко


# вар 3

afk_list = [22,22,33,45,33,1,2,8,6,77,77]


def function(afk_list):
    a = [i*2 for i in afk_list]
    print(a)


# а вот здесь без вызова функции не чего не происходит
# так что такие дела (вывод возврат функции должен быть обязательным)


# задача с работай над ошибками

alf = int(input("enter the number"))


def control(var):
    if var == 6:
        return True
    else:
        return False


res = control(alf)
print(res)

# вроде все ок, но он не печатал не тру не фальш без 55 и 56 строки,
# почему если только один ответ, то можно
# же не давать не res не print
# почему 49 и 55 строчки подгорают

