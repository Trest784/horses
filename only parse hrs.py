import requests
from selenium import webdriver

HOST = 'https://zed.run/'
URL = 'https://zed.run/stud'
HEADERS = {
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_source_html(url):

    driver = webdriver.Chrome(
       executable_path= "C:\Людмила\PycharmProjects\onlyparse\onlyparse\chromedriver.exe"
    )
    driver.maximize_window()

    try:
        driver.get(url=url)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_source_html(url="")

if  __name__ == '_main_':
    main()

# response = requests.get('https://api.zed.run/api/v1/stud/horses').json()

# print(response)









