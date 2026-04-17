from abc import ABC, abstractmethod

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class BaseReport(ABC):
    '''
    Базовый абстрактный класс для всех типов отчётов.
    Каждый новый тип отчёта должен наследоваться от этого класса
    и реализовывать методы filter, sort и print_data.
    '''

    @abstractmethod
    def filter(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Фильтрация данных по критериям конкретного отчёта.

        :param data: Список строк с заголовком первой строкой.
        :return: Отфильтрованный список list[list[str]].
        '''
        pass

    @abstractmethod
    def sort(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Сортировка данных по критериям конкретного отчёта.

        :param data: Список строк.
        :return: Отсортированный список list[list[str]].
        '''
        pass

    @abstractmethod
    def print_data(self, data: list[list[str]]):
        '''
        Вывод данных в терминал.

        :param data: Таблица с заголовком.
        '''
        pass
