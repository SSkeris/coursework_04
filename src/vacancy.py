from abc import ABC, abstractmethod


class Vacancy(ABC):
    """Абстрактный класс для обработки вакансий разный сайтов"""

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass


class VacancyHH(Vacancy):
    """Класс для обработки вакансий с сайта HH.ru"""

    def __init__(self, job):

        self.job = job
        salary = job['salary']

        self.name = job['name'].lower()
        self.experience = str(job['experience']['name'])
        self.employment = job['employment']['name']
        self.place = job['schedule']['name']

        try:
            if salary['currency'] == "USD":
                salary['from'] *= 90
                salary['to'] *= 90
                salary['currency'] = "RUR"
            elif salary['currency'] == "EUR":
                salary['from'] *= 100
                salary['to'] *= 100
                salary['currency'] = "RUR"
            if salary['from'] is None:
                self.salary_from = 0
            else:
                self.salary_from = salary['from']
            if salary['to'] is None:
                self.salary_to = 0
            else:
                self.salary_to = salary['to']
        except:
            self.salary_from = 0
            self.salary_to = 0

    def __repr__(self):
        """Вывод значений атрибутов экземпляра класса"""
        return (f"{self.__class__.__name__}({self.name}, {self.experience}, "
                f"{self.employment}, {self.place}, {self.salary_from} {self.salary_to})")

    def __le__(self, other):
        """Метод для сравнения экземпляров"""
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) <= (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) <= int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) <= int(other.salary_to)
        else:
            return int(self.salary_to) <= int(other.salary_to)

    def __lt__(self, other):
        """Метод для сравнения экземпляров"""
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) < (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) < int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) < int(other.salary_to)
        else:
            return int(self.salary_to) < int(other.salary_to)

    def __gt__(self, other):
        """Метод для сравнения экземпляров"""
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) > (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) > int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) > int(other.salary_to)
        else:
            return int(self.salary_to) > int(other.salary_to)

    def __ge__(self, other):
        """Метод для сравнения экземпляров"""
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) >= (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) >= int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) >= int(other.salary_to)
        else:
            return int(self.salary_to) >= int(other.salary_to)
