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


class JSONSaver(FileSaver):
    """Класс для работы с файлами типа JSON"""

    def __init__(self, data):
        self.data = data

    def save_to_file(self):
        with open('hh_response.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def delete_file(self):
        pass
