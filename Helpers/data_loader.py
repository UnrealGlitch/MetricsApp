import csv

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataLoader:
    '''
    Загрузчик данных из файлов.
    '''

    # Private properties

    __TEST_DATA_PATH = "Data/stats{d}.csv" # Путь к тестовым данным.

    # Life cycle

    def __init__(self):
        pass

    # Public functions

    def load_test_data(self) -> list[list[str]]:
        '''
        Загрузка тестовых данных из файла csv в папке Data/
        Возвращает список данных list[list[str]].
        '''
        return self.load_data(file_path=self.__TEST_DATA_PATH.format(d=1))

    def load_data(self, file_path: str) -> list[list[str]]:
        '''
        Загрузка данных из файла csv по указанному пути file_path.
        Возвращает список данных list[list[str]].
        '''
        rows = []
        with open(file=file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        return rows