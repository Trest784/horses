import requests
from bs4 import BeautifulSoup as bs

get_html = requests.get('https://nb-bet.com/Results'')
get_html.status_code

html = get_html.content
html

soup = bs(html,'html.parser')
soup

sections=soup.select('static')
sections

len(sections)


section = sections[0]

books_block = section.select_one('ol[class=row]')

books = books_block.select('li')
print(len(books))

books_data = []
for book in books:
    image=book.find('div', attrs={'class': 'image_container'}).find('img')['src']
    print(image)
    title = book.find('h3').find('a')['titl