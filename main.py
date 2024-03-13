from src.hh_api import HhAPI
from src.json_saver import JSONSaver
from src.utils import convert_data, cls_to_dict, filter_vacancies, get_by_salary, get_top_vacancies, \
    print_vacancies

hh_api = HhAPI()  # запрашивает вакансии по API
hh_list = hh_api.response().json()["items"]  # получение списка вакансий
vacancies_list = convert_data(hh_list)  # список вакансий класса VacancyHH
list_for_json = cls_to_dict(vacancies_list)  # список словарей, для записи в json
json_saver = JSONSaver(list_for_json)
json_saver.save_to_file()  # сохранение в json
# json_saver.delete_file()  # удаляет содержимое файла json
data_list = json_saver.open_file()  # открытие файла json


def user_interaction():
    """Весь функционал в обёртке"""

    filter_words = input("Введите ключевые слово для фильтрации вакансий: ").lower()
    filtered_vacancies = filter_vacancies(data_list, filter_words)  # фильтруем по слову
    print_vacancies(filtered_vacancies)  # вывод результата
    salary_range = input("Введите диапазон зарплат\n(формат: 'число пробел число' для диапазона, "
                         "\nодно число для начального значения): ")
    ranged_vacancies = get_by_salary(filtered_vacancies, salary_range)  # отбираем по ЗП
    print_vacancies(ranged_vacancies)  # вывод результата
    top_n = 0
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except:
        user_interaction()
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)  # выбираем первые N вакансий для вывода
    print_vacancies(top_vacancies)  # вывод результата


if __name__ == "__main__":
    user_interaction()
