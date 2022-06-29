#1 создать список из 10 четных чисел и вывести его с помощью for

list_a = [2,4,6,8,10,12,14,16,18,20]
for i in list_a:
    print(i)

#2   Создайте список из 5 элементов. Сделайте срез от второго индекса до четвертого

list_b = [1,3,5,6,7]
print(list_b[2:5])

# Создайте список из введенной пользователем строки и удалите из него символы 'a', 'e', 'o'

list_c = ["kak", "eto","otobrat"] 
# del list_c[1]
print(list_c)

# вот это полная дерьмо я же взял правильную команду del  но удаляет слово это полностью
# я думаю проблема в том что я вогнал буквы в слова
# я пытался  слова представить как вложенные списки и вытскивать но не получилось
# вообще я могу удалить слова а не буквы  если вместо слов убрать буквы

# Alexey: есть 2 метода решения
# 1. Если пользоваться твоим списком то через цикл

for i in range(len(list_c)):
    # list_c[i] = list_c[i].replace('a', '')
    # list_c[i] = list_c[i].replace('e', '')
    # list_c[i] = list_c[i].replace('o', '')

    list_c[i] = list_c[i].replace('a', '').replace('e', '').replace('o', '')
    
print(list_c)

# Alexey:
# 2. Если правильно следовать задаче
input_text = input('Вводи строку:\n')
text_list = list(input_text)

# print(text_list)
for i in range(text_list.count('a')):
    text_list.remove('a')

for i in range(text_list.count('a')):
    text_list.remove('e')

for i in range(text_list.count('a')):
    text_list.remove('o')
print(text_list)


# Пришел в голову классный 3 способ с def
text_list2 = list(input_text)
def remove_all(in_list, substring):
    for i in range(in_list.count(substring)):
        in_list.remove(substring)

remove_all(text_list2, 'a')
remove_all(text_list2, 'e')
remove_all(text_list2, 'o')
# print(text_list2)

