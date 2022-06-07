# импортируем библиотеку request для работы с данными в сети
import requests
import pprint  # для печати в красивом формате
x=[]
all_zp = 0 # здесь будем накапливать сумму всех зарплат
all_n = 0  # здесь будем накапливать количество суммированных зарплат
url = 'https://api.hh.ru/vacancies' # url-адрес запроса
par = {'text': 'Python developer', 'area':'1','per_page':'10', 'page':1} # параметры запроса 'интернет маркетолог'
r = requests.get(url, params=par) # результат get-запроса сохраняем в переменной r
e=r.json()  #  переменную r преобразовываем в формат json и сохраняем в переменной e
x.append(e) # в массив x дописываем переменную e
#pprint.pprint(x)

# СЧИТАЕМ КОЛИЧЕСТВО КОМПЕТЕНЦИЙ:
for j in x:         # пробегаем в цикле по items
    n_python = 0
    n_django = 0
    n_flask = 0
    n_sqlalchemy =0
    y = j['items']  # присваиваем переменной y текущеезначение  items
    for i in y: #цикл, перебирает объекты, т.е перебирает вакансии
        list_data = []
        skill = i['snippet']
        for k,  v in skill.items():
            list_data.append(k + ':' + str(v))
        stroka = " ".join(list_data)
        stroka = stroka.lower()
        if 'python' in stroka:
            n_python += 1
        if 'django' in stroka:
            n_django += 1
        if 'flask' in stroka:
            n_flask += 1
        if 'sqlalchemy' in stroka:
            n_sqlalchemy += 1
itog = n_python + n_django + n_flask + n_sqlalchemy
print('Количество Python: ', n_python)
print('Количество Django: ', n_django)
print('Количество Flask: ', n_flask)
print('Количество Sqlalchemy: ', n_sqlalchemy)
print()
print('Доля Python: ', 100 * n_python/itog)
print('Доля Django: ', 100 * n_django/itog)
print('Доля Flask: ', 100 * n_flask/itog)
print('Доля Sqlalchemy: ', 100 * n_sqlalchemy/itog)

print() # пустая строка - чтобы отделить

# СЧИТАЕМ СРЕДНЮЮ ЗАРПЛАТУ:
for j in x:         # пробегаем в цикле по items
    y = j['items']  # присваиваем переменной y текущеезначение  items
    n=0 #объявляем переменную n для подсчета, количества итераций цикла перебирающего зарплаты в вакансиях
    sum_zp=0 #объявляем переменную sum_zp для подсчета, суммы зарплат в вакансиях
    for i in y: #цикл, перебирает объекты, т.е перебирает вакансии
        if i['salary'] !=None: # делаем ТОЛЬКО для техстрок, где есть данные по зарплате
            tek_zp = i['salary'] # текущую зарплату записываем впеременную  tek_zp
            s=i['salary'] #записываем текущее значение зарплаты в переменную s
            if s['from'] !=None: #проверяем есть ли в вакансии данные по минимальной зп
                n += 1 # считаем количество обработанных вакансий в которых указана минимальная ЗП
                s['from'] #получаем минимальную ЗП по ключу from
                sum_zp += s['from']  #считаем сумму ЗП по вакансиям
    all_zp += sum_zp   #добавляем сумму зп по итерации цикла
    all_n +=n   #добавляем сумму n по итерации цикла
#print(all_n)  # печатаем количество суммированных зарплат
av_zp=all_zp / all_n  #считаем среднюю ЗП
print('Средняя зарплата: ', av_zp) # печатаем среднюю зарплату



