import requests
import pprint  # для печати в красивом формате

url = 'https://api.hh.ru/vacancies' # url-адрес запроса
params = {                         # задаем параметры запроса
    'text' : 'NAME: Python',
    'page' : 1     # выводим на страницу 1
}

result = requests.get(url, params=params).json() # результат запроса помещаем в result в обычном формате
items = (result['items'])
#pprint.pprint(items[0])
url = items[0]['url']  #'key_skills': [{'name': 'Linux'},{'name': 'Git'},{'name': 'Python'},{'name': 'SQL'},{'name': 'Unix'}],

for item in items:
    url = item['url']
    result = requests.get(url).json()
    print(result["key_skills"])
