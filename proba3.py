import requests
import pprint  # для печати в красивом формате

DOMAIN = 'https://api.hh.ru/'  # будем работать с api
url_vacancies = f'{DOMAIN}vacancies'  # адрес для  получения вакансий (из документации по api)

params = {                         # задаем параметры запроса
    #'text' : 'NAME: (Python OR Java)  AND COMPANY_NAME: (SBERBANK OR GAZPROM OR YANDEX) AND (DJANGO OR SPRING)',
    'text' : 'NAME: (Python OR Java) AND (DJANGO OR SPRING)',
    #'area': 95, # По городу Москва - 1,  54 - Красноярск, 66 - Нижний Ноывгород, 96 - Ижевск (24)
    # есть страницы, так как данных много
    'page' : 1     # выводим на страницу 1
}

result = requests.get(url_vacancies, params=params).json() # результат запроса помещаем в result в формате JSON
pprint.pprint(result) # печатаем все найденные записи
#print(result['items'][0]['alternate_url'])