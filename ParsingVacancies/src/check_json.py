import json
import os
from src.vacancy import Vacancy

FILE = 'vacancies.json'

"""
Класс для взаимодействия с json файлом, содержит статические методы
"""


class JsonAgent:
    """
    Метод для проверки на уже существующие вакансии в файле json
    """

    @staticmethod
    def check_for_repeat(vacancy: Vacancy):
        try:
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []  # Если файл не существует или пуст, создаем пустой список вакансий.

        for v in vacancies:
            if v['title'] == vacancy.title and v['url'] == vacancy.url and \
                    v['pay'] == vacancy.pay and v['requirement'] == vacancy.requirement:
                return False  # Вакансия уже существует, не добавляем ее.

        return True  # Вакансии с такими данными нет, можно добавить.

    """
    Метод для добавления вакансии в файл json
    """

    @staticmethod
    def add_vacancy(vacancy: Vacancy):
        if not os.path.exists(FILE):
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump([], f)
                print("Файл vacancies.json был создан.")

        print("Попытка добавить вакансию")
        if JsonAgent.check_for_repeat(vacancy):
            with open(FILE, 'r', encoding='utf-8') as f:
                try:
                    vacancies = json.load(f)
                except json.JSONDecodeError:
                    print("Файл vacancies.json поврежден. Создаю новый файл.")
                    with open(FILE, 'w', encoding='utf-8') as new_f:
                        json.dump([], new_f)
                    vacancies = []

            vacancies.append(vacancy.json())
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)
            print("Вакансия успешно добавлена")
            return True
        else:
            print("Произошла ошибка при добавлении вакансии")
            return False

    """
    Метод, который удаляет вакансию из файла по её названию. 
    Возвращает true если вакансия найдена и удалена, иначе False.
    """

    @staticmethod
    def delete_vacancy_by_title(title):
        try:
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Произошла ошибка при загрузке вакансий.")
            return False

        f = False
        for vacancy in vacancies:
            if vacancy['title'] == title:
                vacancies.remove(vacancy)
                f = True
                break
        if f:
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)
            return True
        else:
            return False

    """
    Метод, который выводит в консоль названия всех вакансий в файле
    """

    @staticmethod
    def show_vacancies_title():
        try:
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
            if not vacancies:
                print("Файл с вакансиями пуст.")
            else:
                for vacancy in vacancies:
                    print(vacancy['title'])
        except (FileNotFoundError, json.JSONDecodeError):
            print("Произошла ошибка при загрузке вакансий.")

    """
    Метод, который очищает json файл
    """

    @staticmethod
    def clear_json():
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    """
    Метод, который выводит в консоль информацию о найденной по названию вакансии
    """

    @staticmethod
    def show_info_by_title(title):
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = Vacancy.all_from_json(f)
        for vacancy in vacancies:
            if vacancy.title == title:
                vacancy.show_info()
                break
