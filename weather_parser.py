import requests
from bs4 import BeautifulSoup

url1 = 'https://yandex.ru/pogoda/?lat=55.685603&lon=37.746871'
url2 = 'https://yandex.ru/pogoda/?lat=59.93909836&lon=30.31587601'
url3 = 'https://yandex.ru/pogoda/?lat=55.03020096&lon=82.92043304'
url4 = 'https://yandex.ru/pogoda/?lat=56.8380127&lon=60.59747314'
resp1 = requests.get(url1)
resp2 = requests.get(url2)
resp3 = requests.get(url3)
resp4 = requests.get(url4)
bs1 = BeautifulSoup(resp1.text, 'lxml')
bs2 = BeautifulSoup(resp2.text, 'lxml')
bs3 = BeautifulSoup(resp3.text, 'lxml')
bs4 = BeautifulSoup(resp4.text, 'lxml')
temperatura1 = bs1.find_all('span', class_="temp__value temp__value_with-unit") [1]
temperatura2 = bs2.find_all('span', class_="temp__value temp__value_with-unit") [1]
temperatura3 = bs3.find_all('span', class_="temp__value temp__value_with-unit") [1]
temperatura4 = bs4.find_all('span', class_="temp__value temp__value_with-unit") [1]
text1 = f'температура в Москве на сегодня: {temperatura1.text}°'
text2 = f'температура в Санкт-Петербурге на сегодня: {temperatura2.text}°'
text3 = f'температура в Новосибирске на сегодня: {temperatura3.text}°'
text4 = f'температура в Екатеринбурге на сегодня: {temperatura4.text}°'
