import json
import os
from abc import ABC, abstractclassmethod

import requests
from dotenv import load_dotenv


class Api(ABC):

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_vacancies(self, word: object):
        pass


class HhApi(Api):

    def __init__(self, count):
        """
        Конструктор с входным параметром количество вакансий, который устанавливает параметры для гет-запросов
        """
        self.params = {
            'per_page': count,
            'area': 1,
            'page': 1
        }
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, words):
        """
        Метод получения вакансий и преобразования их из json в словари
        """
        self.params['text'] = words
        r = requests.get(self.url, params=self.params)
        vacancies = json.loads(r.text)["items"]
        return vacancies


class SuperJobApi(Api):

    def __init__(self, count):
        """
        Конструктор с входным параметром количества вакансий,
        который устанавливает параметры и заголовки для гет-запросов
        """
        load_dotenv()
        __api_token: str = os.environ.get("SJ_API_KEY")
        self.headers = {
            "X-Api-App-Id": f"{__api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.params = {
            'count': count,
            'page': 1,
            'town': 'Moscow'
        }
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, words):
        """
        Метод для получения вакансий и преобразования их из json в словари
        """
        self.params['reywords'] = words
        r = requests.get(self.url, params=self.params, headers=self.headers)
        vacancies = json.loads(r.text)['objects']
        return vacancies
