from pandas import DataFrame as df
import pprint
import requests
import http.client



stop_list_soft = ['или']
stop_list_hard = ['масса']



http.client._MAXHEADERS = 1000

from bs4 import BeautifulSoup


def parse_table(table):  # Функция разбора таблицы с вопросом
    name = ''
    ingrI = []
    ingrII = []
    ingrIII = []

    return (table)


def process_url(url):
    r = requests.get(url)

    # отправляем HTTP запрос и получаем результат
    soup = BeautifulSoup(r.text, features="html.parser")  # Отправляем полученную страницу в библиотеку для парсинга
    tables = soup.find('table', {'class': 'tabstyle3'})  # Получаем все таблицы с вопросами
    dish = soup.find_all('h1')[0].text

    td_contents = []
    table = soup.find('table')

    for td in table.find_all('td'):
        td_contents.append(td.text.strip())

    row = []
    ingredients = []
    k = 0
    for i in td_contents[10:]:
        row.append(i)
        if k != 6:
            k += 1
        else:
            k = 0
            ingredients.append(row)
            row = []


    print(ingredients)
    recipe = ''

    for word in soup.find_all('p', {'class': 'word'}):
        recipe += word.text
    index_to_remove = False
    # analyze
    for i in range(len(ingredients)):
        if ingredients[i][0].strip().lower().startswith('или'):
            if len(ingredients[i][0])<4:
                ingredients[i+1].append(i - 1)
            else:
                ingredients[i].append(i - 1)
        if 'Гарнир' in ingredients[i][0]:
            index_to_remove = i



    if index_to_remove:
        ingredients.pop(index_to_remove)

    print(dish)
    pprint.pprint(ingredients)
    print(recipe)


url = 'https://interdoka.ru/kulinaria/1982/10_bluda_miaso/2_garenoe/9.html'  # url страницы

for i in range(10):
    url = f'https://interdoka.ru/kulinaria/1982/10_bluda_miaso/2_garenoe/{i+1}.html'
    process_url(url)
