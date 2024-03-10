import json

from src.vacancy import VacancyHH


def convert_data(data: list) -> list:
    """Принимает список словарей с данными запроса, возвращает список экземпляров класса VacancyHH"""
    new_list = []
    for n in data:
        new_list.append(VacancyHH(n))
    return new_list


def cls_to_dict(data: list) -> list:
    """Принимает список экземпляров класса VacancyHH, возвращает список словарей, для записи в json"""
    new_list = []
    for obj in data:
        new_dict = {
            'name': obj.name,
            'experience': obj.experience,
            'employment': obj.employment,
            'place': obj.place,
            'salary_from': obj.salary_from,
            'salary_to': obj.salary_to
        }
        new_list.append(new_dict)
    return new_list


def filter_vacancies(dict_list: list, filter_words) -> list:
    """Получает список и фильтрует его по критерию пользователя, возвращает список"""
    new_list = []
    for d in dict_list:
        for word in filter_words.split():
            if d['name'].find(word) != -1:
                new_list.append(d)
        if not filter_words:
            new_list.append(d)
    return new_list


def get_by_salary(dict_list, salary):
    """Выбирает словари, где средняя зарплата больше или равна запросу"""
    if not isinstance(salary, int):
        salary = 0
    new_list = []
    for i in dict_list:
        if (i['salary_from'] + i['salary_to']) / 2 >= salary:
            new_list.append(i)
    sorted_list = sorted(new_list, key=lambda d: (d['salary_from'] + d['salary_to']) / 2, reverse=True)
    return sorted_list


def get_top_vacancies(dict_list, number):
    """Выбирает N вакансий из списка словарей"""
    new_list = []
    count = 0
    if number is not None:
        try:
            for d in dict_list:
                if count >= number:
                    break
                else:
                    count += 1
                    new_list.append(d)
            return new_list
        except:
            return new_list
    else:
        return dict_list


def print_vacancies(dict_list):
    """Вывод результата работы программы"""
    count = 0
    for d in dict_list:
        if d['salary_from'] and d['salary_to'] == 0:
            print(f'{count + 1}) Вакансия: {d['name']}\n'
                  f'Требования: {d['experience']}\n'
                  f'График работы: {d['employment']}\n'
                  f'Офис/удалёнка: {d['place']}\n'
                  f'Зарплата: Договорная\n')
            count += 1
        else:
            print(f'{count + 1}) Вакансия: {d['name']}\n'
                  f'Требования: {d['experience']}\n'
                  f'График работы: {d['employment']}\n'
                  f'Офис/удалёнка: {d['place']}\n'
                  f'Зарплата: {d['salary_from']}-{d['salary_to']}\n')
            count += 1
