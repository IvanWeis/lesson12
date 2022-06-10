import requests
from bs4 import BeautifulSoup


url = 'https://dedmorozural.ru/novosti'

response = requests.get(url)
# print(response)
# print(response.status_code) # 200 - успешно
# print(response.text) # выводит ВСЮ html-страницу

soup = BeautifulSoup(response.text, 'html.parser') # вытаскивает красивую html-страницу, дальше ее разбираем по косточкам
# print(page_html)

                           # ВВОДНАЯ ЧАСТЬ ЗАНЯТИЯ (ЗНАКОМСТВО С ИНСТРУМЕНТАМИ)

# print(soup.a) # находит первый тег  a
# print(soup.a.text) # текст первого тега  a  типа  string (строка)
# print(type(soup.a.text)) # текст первого тега  a

# a_tags = soup.find_all('a') # находит ВСЕ тэги a
#
# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих тегов
# a_tags = soup.find_all('a') # находит ВСЕ тэги a

# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих теговa_tags = soup.find_all('a') # находит ВСЕ тэги aa_tags = soup.find_all('a') # находит ВСЕ тэги a
#
# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих тегов
# a_tags = soup.find_all('a') # находит ВСЕ тэги a

# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих теговa_tags = soup.find_all('a') # находит ВСЕ тэги a
#
# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих тегов
# a_tags = soup.find_all('a') # находит ВСЕ тэги a
#
# for link in soup.find_all('p'):  # находим все теги  a
#     print(link.text)  # печатаем текст из этих тегов

big_body_div = soup.find('div', class_ = 'modulebody1') # поиск по классу (class)
# print(big_body_div)

# можно искать в уже найденном:
bigbodydiv3 = big_body_div.find('div', class_ = 'modulebody3')
print(bigbodydiv3)

            # РЕШЕНИЕ ЗАДАЧИ (ВЫТАСКИВАЕМ НОВОСТИ):
# смотри в файле   new_parser