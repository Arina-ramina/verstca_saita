import json

FILE = 'vacancies.json'

"""Класс для хранения и работы с информацией о вакансиях"""


class Vacancy:
    """
    Конструктор, принимает название, ссылку, заработную плату, требования
    """

    def __init__(self, title, url, pay, requirement) -> None:
        self.title = title
        self.url = url
        self.pay = pay
        self.requirement = requirement

    """
    Метод, который возвращает информацию о вакансии в виде словаря
    """

    def json(self):
        return {
            'title': self.title,
            'url': self.url,
            'pay': self.pay,
            'requirement': self.requirement,
        }

    """
    КлассМетод, который создает вакансию на основе словаря
    """

    @classmethod
    def from_json(cls, params):
        return cls(params['title'], params['url'], params['pay'], params['requirement'])

    """
    КлассМетод, который создает массив вакансий на основе информации из json файла
    """

    @classmethod
    def all_from_json(cls):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        output = []
        for vacancy in vacancies:
            tmp = Vacancy.from_json(vacancy)
            output.append(tmp)
        return output

    """
    Метод, который выводит в консоль информацию о вакансии
    """

    def show_info(self):
        print(self.title)
        print(self.url)
        print(f'Заработная плата {self.pay}')
        print(self.requirement)

    def __repr__(self) -> str:
        return f"{self.title}\n{self.pay}\n{self.url}\n{self.requirement}"


class VacancyAgent:
    """
    Метод, который получает на вход словарь из superjob и возвращает массив Vacancy
    """

    @staticmethod
    def pars_super_job(vacancies):
        output = []
        for vacancy in vacancies:
            if vacancy['payment_from'] is not None:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], vacancy['payment_from'], vacancy['candidat'])
            elif vacancy['payment_to'] is not None:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], vacancy['payment_to'], vacancy['candidat'])
            else:
                tmp = Vacancy(vacancy['profession'], vacancy['link'], '0', vacancy['candidat'])
            output.append(tmp)
        return output

    """
    Метод, который получает на вход словарь из hh.ru и возвращает массив Vacancy
    """

    @staticmethod
    def pars_hh_ru(vacancies):
        output = []
        for vacancy in vacancies:
            if vacancy['salary'] is not None:
                if vacancy['salary']['from'] is not None:
                    tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', vacancy['salary']['from'],
                                  vacancy['snippet']['requirement'])
                else:
                    tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', vacancy['salary']['to'],
                                  vacancy['snippet']['requirement'])
            else:
                tmp = Vacancy(vacancy['name'], f'https://hh.ru/vacancy/{vacancy["id"]}', "0",
                              vacancy['snippet']['requirement'])
            output.append(tmp)
        return output

    """
    Метод, который возвращает названия вакансий по заданным словам для поиска
    """

    @staticmethod
    def filter_vacancies_by_keywords(vacancies: list, key_words=None):
        if key_words is None:
            key_words = []
        output = []
        for vacancy in vacancies:
            title = [x.lower() for x in vacancy.title.split()]
            try:
                requiremets = [x.lower() for x in vacancy.requirement.split()]
            except:
                requiremets = []
            for key_word in key_words:
                if key_word.lower() in title or key_word.lower() in requiremets:
                    output.append(vacancy.title)
                    break
        return output

    """
    Метод, который возвращает названия вакансий по заданному диапазону заработной платы
    """

    @staticmethod
    def filter_vacancies_by_salary(vacancies: list, sfrom, sto):
        output = []
        for vacancy in vacancies:
            try:
                if sfrom <= vacancy.pay <= sto:
                    output.append(vacancy.title)
            except:
                pass
        return output
