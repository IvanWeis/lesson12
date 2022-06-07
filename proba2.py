import requests
import pprint  # для печати в красивом формате

DOMAIN = 'https://api.hh.ru/'  # будем работать с api
url_vacancies = f'{DOMAIN}vacancies'  # адрес для  получения вакансий (из документации по api)

params = {                         # задаем параметры запроса
    #'text' : 'C# developer',
    'text' : 'Python developer',
    'area': 95, # По городу Москва - 1,  54 - Красноярск, 66 - Нижний Ноывгород, 96 - Ижевск (24)
    # страница
    'page' : 1      # выводим на страницу 1
}

#result = requests.get(url_vacancies, params=params).json() # результат запроса помещаем в result в формате json
result = requests.get(url_vacancies, params=params) # результат запроса помещаем в result в обычном формате
# pprint.pprint(result) # выводим для проверки
# items = result['items'] # берем для исследования толькосвойство items
# first = items[0] # берем свойство items перой записи (первого элемента)
# pprint.pprint(first) # печатаем содержимое первой записи (первого элемента)
pprint.pprint(result.json()) # печатаем все найденные записи в формате json
# pprint.pprint(result.text) # печатаем все найденные записи в формате text
#'snippet' - с какими инструментами работает
# print(result.text['snippet'])
#print(result.text)