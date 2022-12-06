import pickle       # модуль для работы с любыми типами данных
import os.path      # мщдуль для корректной работы с путями


class Film:
    def __init__(self, title, genre, producer, year_of_issue, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year_of_issue = year_of_issue
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):                         # Для представлеения каталога фильмов в виде
        return f"{self.title} ({self.genre})"


class FilmModel:                               # Для сбора и сохранения всех созданных и приходящих данных
    def __init__(self):
        self.db_films = 'db_films.txt'
        self.films = self.load_data()          # загрузка начального списка {} фильмов

    def add_film(self, dict_film):                                                           # (* - распаковка словаря)
        film = Film(*dict_film.values())   # создаём экземпляр класса Film на основе значений словаря, введ-ых польз-лем
        self.films[film.title] = film      # сохраняем эти данные в словарь self.films в model

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):  # получение данных фильма по ключу, кот. введёт польз- ль(user_title)
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "продюсер": film.producer,
            "год выпуска": film.year_of_issue,
            "длительность": film.duration,
            "студия": film.studio,
            "актёры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)        # метод pop, тк этот метод возвращает удалённый элемент

    def load_data(self):                         # метод загрузки текущих данных
        if os.path.exists(self.db_films):        # если существует файл db_file
            with open(self.db_films, 'rb') as f:
                return pickle.load(f)            # модуль pickle даёт возможность работы с любыми типами данных в Питоне
        else:
            return dict()                        #  иначе - возвращаем пустой словарь
    #
    def save_data(self):
        with open(self.db_films, 'wb') as f:
            pickle.dump(self.films, f)           # сохранение данных из self.films

