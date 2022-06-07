# GET - запрос на сайт DNS:
#  https://www.dns-shop.ru/catalog/251c82c88ed24e77/smart-chasy-i-braslety/?price=1001-5000&brand=amazfit
# указана страница - smart-chasy-i-braslety и параметры фильтра: Цена, Брэнд

# POST - запрос - в строке видим только часть, а остальная часть - невидимая (скрытая)
# CRUD  Create, Read, Update, Delete   Read - одной записи и Read - списка
# REST - расширение http протокола. Кроме GET и POST есть еще  (всего 9 штук)
# для того, чтобы пользоваться REST-запрсами импортируем библиотеку request (сначала ее надо установить)
import requests

DOMAIN1 = 'https://www.dns-shop.ru/' # адрес сайта DNS
DOMAIN2 = 'http://weisivan.ru/index.html'      # адрес главной страницы моего сайта
DOMAIN3 = 'https://hh.ru/'      # адрес главной страницы hh

result = requests.get(DOMAIN3)
print(result)  # выводится: <Response [200]>  Response - объект, с которым можно работать, 200 - успешно
print(result.status_code) # код ответа
print(result.text) # текст ответа

# GET - считываем всю информацию, POST - отправляем информацию PUT - меняем одну запись, DElETE - удаляем одну запись