import csv

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataLoader:
    '''
    Загрузчик данных из файлов.
    '''

    # Life cycle

    def __init__(self):
        pass

    # Public functions

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