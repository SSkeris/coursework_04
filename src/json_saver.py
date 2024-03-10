import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

    @abstractmethod
    def open_file(self):
        pass


class JSONSaver(FileSaver):
    """Класс для работы с файлами типа JSON"""

    def __init__(self, data):
        self.data = data

    def save_to_file(self):
        """Сохранение в json"""
        with open('hh_response.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def delete_file(self):
        """Удаляет содержимое файла json"""
        with open("hh_response.json", "w") as file:
            file.truncate()

    def open_file(self):
        """Распаковывает json файл для выборки пользователя"""
        with open('hh_response.json', 'r', encoding='utf-8') as f:
            return json.load(f)
