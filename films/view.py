#   Визуальная связь Контроллера с пользователем

def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output
        return wrap
    return wrapper



class UserInterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):                          # ожидание ответа ползователя
        print("Действия с фильмами:")
        print("1 - добавление фильма"
            "\n2 - каталог фильмов"
            "\n3 - просмотр определённого фильма"
            "\n4 - удаление фильма"  
            "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Добавление фильма')
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актёры": None
        }
        for key in dict_film:
            dict_film[key] = input(f'Введите {key} фильма: ')
        return dict_film

    @add_title("Каталог фильмов")
    def show_all_films(self, films):
        for i, film in enumerate(films, start=1):
            print(f"{i}. {film}")

    @add_title('Ввод названия фильма')
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удалён")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

