from bs4 import BeautifulSoup
import requests
import csv
import re


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def refined(s):
    rat = re.sub(r"\D+", "", s)
    return rat


def write_csv(data):
    with open('recommended_plugins.csv', 'a') as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow((data['name'], data['description'], data['rating'], '\n'))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all("section", class_="plugin-section")[3]
    boxes = p1.find_all("article")

    for box in boxes:
        name = box.find("h3").text
        description = box.find("div", class_="entry-excerpt").text
        rating = box.find("span", class_="rating-count").find("a").text
        rat = refined(rating)
        print(name, description, rat, '\n')

        data = {'name': name, 'description': description, 'rating': rat}
        write_csv(data)


def main():
    url = "https://ru.wordpress.org/plugins/"
    get_data(get_html(url))

if __name__ == '__main__':
    main()


#  ВЫВОД:
# C:\Users\Dmitry\Scripts\HomeWork\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/HomeWork/D_Z_Parsing.py
# Contact Form 7
# Ещё один плагин контактных форм. Простой, но гибкий.
#  1981
#
# Yoast SEO
# Улучшите SEO вашего WordPress: поработайте над качеством контента и получите полностью оптимизированный WordPress-сайт с помощью…
#  27530
#
# Elementor — конструктор сайтов
# В конструкторе сайтов Elementor есть всё: визуальный конструктор страниц работающий на принципе перетащи и вставь,…
#  6373
#
# Classic Editor
# Включает предыдущую «классическую» версию редактора и экран редактирования записей в старом стиле, с TinyMCE, полями…
#  1091


Process finished with exit code 0
