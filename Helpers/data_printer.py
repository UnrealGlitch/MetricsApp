from tabulate import tabulate

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataPrinter:
    '''
    Класс, специализирующийся на выводе данных на экран.
    '''

    # Life cycle

    def __init__(self, report_name: str):
        self.report_name = report_name # Заголовок выводимой в терминал таблицы.

    # Public functions

    def print_data(self, data):
        '''
        Вывод в терминал отсортированных данных.
        '''
        headers = data[0]
        rows = data[1:]
 
        print(f"\n{self.report_name}")
        print(tabulate(rows, headers=headers, tablefmt="psql"))