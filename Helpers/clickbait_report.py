from tabulate import tabulate
from Helpers.base_report import BaseReport

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class ClickbaitReport(BaseReport):
    '''
    Отчёт по кликбейт-заголовкам.
    Фильтрует по ctr > 15 и retention_rate < 40.
    Сортирует по убыванию ctr.
    Выводит колонки: title, ctr, retention_rate.
    '''

    # Private properties

    __REPORT_NAME = "Clickbait Report"
    __CTR = 15
    __RETENTION = 40

    # Life cycle

    def __init__(self):
        pass

    # Public functions

    def filter(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Фильтрация строки по критериям ctr > 15 и retention_rate < 40.
        Остаются только колонки title, ctr, retention_rate.

        :param data: Список строк с заголовком первой строкой.
        :return: Отфильтрованный список list[list[str]] с заголовком в начале.
        '''
        output_list = []
        title_index, ctr_index, retention_index = self.__get_column_indices(data[0])

        for i in range(1, len(data)):
            row = data[i]
            if float(row[ctr_index]) > self.__CTR and float(row[retention_index]) < self.__RETENTION:
                new_row = [row[title_index], row[ctr_index], row[retention_index]]
                output_list.append(new_row)
        return [data[0]] + output_list

    def sort(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Сортировка строки по убыванию значения поля ctr.

        :param data: Список строк с заголовком первой строкой.
        :return: Отсортированный список list[list[str]] с заголовком в начале.
        '''
        if len(data) == 0:
            return data

        headers = data[0]
        _, ctr_index, _ = self.__get_column_indices(headers=headers)
        sorted_rows = sorted(data[1:], key=lambda row: float(row[ctr_index]), reverse=True)

        return [headers] + sorted_rows

    def print_data(self, data: list[list[str]]):
        '''
        Вывод данных в терминал в виде таблицы.

        :param data: Список строк с заголовком первой строкой.
        '''
        print(f"\n{self.__REPORT_NAME}")
        print(tabulate(data[1:], headers=data[0], tablefmt="psql"))

    # Private functions

    def __get_column_indices(self, headers: list[str]) -> tuple[int, int, int]:
        '''
        Получения индексов колонок title, ctr и retention_rate по строке заголовков.

        :param headers: Список названий колонок.
        :return: Кортеж (title_index, ctr_index, retention_rate_index).
        '''
        ctr_index = -1
        retention_rate_index = -1
        title_index = -1
        for i in range(len(headers)):
            if headers[i] == "ctr":
                ctr_index = i
            elif headers[i] == "retention_rate":
                retention_rate_index = i
            elif headers[i] == "title":
                title_index = i
        return (title_index, ctr_index, retention_rate_index)