from view import UserInterface
from model import FilmModel


class Controller:                              # Посредник между view и model
    def __init__(self):
        self.film_model = FilmModel()          # model( создание экземпляра класса FilmModel)
        self.user_interface = UserInterface()  # view( экз. класса UserInterface)

    def run(self):
        answer = None                                   # переменная для ввода пользователем
        while answer != "q":
            answer = self.user_interface. wait_user_answer()  # возвращаемое значение пользователя
            self.check_user_answer(answer)              # вызов метода check_user_answer

    def check_user_answer(self, answer):                # Фун-я. проверки ответа пользователя
        if answer == "1":
            film = self.user_interface.add_user_film()  # обращение во view( вернётся то, что ввёл пользователь)
            self.film_model.add_film(film)
        elif answer == "2":
            films = self.film_model.get_all_films()
            self.user_interface.show_all_films(films)
        elif answer == '3':
            film_title = self.user_interface.get_user_film()        # просим польз-ля ввести фильм для просмотра
            try:
                film = self.film_model.get_single_film(film_title)  # метод в моделе, чтобы достать этот фильм из модели
            except KeyError:                                        # и показать пользов-лю
                self.user_interface.show_incorrect_title_error(film_title)
            else:                                            #  отработает в случае отработки try
                self.user_interface.show_single_film(film)
        elif answer == '4':
            film_title = self.user_interface.get_user_film()     # просим польз-ля ввести название статьи
            try:
                title = self.film_model.remove_film(film_title)  # Достаём из model, указывая фильм, что ввёл польз-ль
            except KeyError:                                     # через view
                self.user_interface.show_incorrect_title_error(film_title)

            else:
                self.user_interface.remove_single_film(title)
        elif answer == 'q':
            self.film_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
