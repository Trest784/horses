from sre_constants import SUCCESS
from regex import F
import requests # извлечения библиотеки
from bs4 import BeautifulSoup as bs #извлечения бютифул супа из бс 4

import os

link_res = 'https://books.toscrape.com/'
get_html = requests.get(link_res) #запрос о выдаче данных с сайта
get_html.status_code #проверка статуса запроса

html = get_html.content #запрос на выдачу контента через хтмл
html # зачем это здесь??????

soup = bs(html,'html.parser') #работает суп) он говорит иследуй хтмл
soup #зачем

sections=soup.select('section') #выбор поля парсинга
sections

len(sections) #не понимаю
try:
    os.mkdir('downloads')
except:
    pass

section = sections[0] #выбор зоны парсинга?

books_block = section.select_one('ol[class=row]') #определение зоны класса парсинга

books = books_block.select('li') #непонимаю
print(len(books)) #принт чего
books_data = {}
id = 0
for book in books:
    id += 1
    image = book.find('div', attrs={'class': 'image_container'}).find('img')['src']
    # print(image)
    title = book.find('h3').find('a')['title']

    books_data[id] = {'name': title, 'link_res': link_res + image}
    # print(books_data)
    r = requests.get(books_data[id]['link_res'])
    path_download = os.getcwd() + '/downloads/' + title
    # print(path_download)
    print('Start downloading "{}" ...'.format(title))
    with open(path_download+'.'+image.split('.')[-1], 'wb') as f:
        f.write(r.content)
    print('Success!')
    #весь кусок кода с 26 по 30 строку не понимаю , что в итоге я напарсил не понятно
