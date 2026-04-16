import csv

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataLoader:
    '''
    Загрузчик данных из файлов.
    '''

    # Properties

    TEST_DATA_PATH = "Data/stats{d}.csv" # Путь к тестовым данным.

    # Life cycle

    def __init__(self):
        pass

    # Public

    def load_test_data(self):
        '''
        Загрузка тестовых данных из файла csv в папке Data/
        '''
        self.load_data(file_path=DataLoader.TEST_DATA_PATH.format(d=1))
        print()
        self.load_data(file_path=DataLoader.TEST_DATA_PATH.format(d=2))

    def load_data(self, file_path: str):
        '''
        Загрузка данных из файла csv по указанному пути file_path.
        '''
        with open(file=file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    
    # Private
