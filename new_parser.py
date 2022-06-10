import requests
from bs4 import BeautifulSoup

domain = 'https://dedmorozural.ru'
url = f'{domain}/novosti'
response = requests.get(url) # результат запроса в виде текста страницы помещаем в переменную response
soup = BeautifulSoup(response.text, 'html.parser') # делаем красивую html-страницу (суп)
# print(soup)  # для проверки
news_a = soup.find_all('a', class_ = 'con_titlelink') # в классе находим ВСЕ теги a, содержащие новости
#print(news_a)  # для проверки

#for one_news_a in news_a[:1]:  # пробегаем по найденным тегам a (новостным ссылкам)
for one_news_a in news_a:  # пробегаем по найденным тегам a (новостным ссылкам)
     text = one_news_a.text
     href = one_news_a.get('href')
  #   print(text, href)
    # шаг 2
     url = f"{domain}{href}"
     response = requests.get(url) # делаем запрос уже по полученной ссылке откаждого a
     # далее разбираем страницу с одной новостью:
     soup = BeautifulSoup(response.text, 'html.parser') # формируем новый суп
     # получаем заголовки, которые хранятся в теге strong (нам повезло, т.к. задача упростилась)
 #    print(soup)

     news_titles_tag = soup.find_all('div', class_ = 'con_desc') # делаем суп из тегов strong con_desc
     print(news_titles_tag)
    #  for title_tag in news_titles_tag: # пробегаем по списку заголовков
    #      print(title_tag.text) # текст каждого заголовкаfor title_tag in news_titles_tag: # пробегаем по списку заголовков
    #