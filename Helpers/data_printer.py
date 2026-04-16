from rich.console import Console
from rich.table import Table

if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataPrinter:
    '''
    Класс, специализирующийся на выводе данных на экран.
    '''

    # Private properties

    __TABLE_NAME = "Clickbait Report" # Заголовок выводимой в терминал таблицы.

    # Life cycle

    def __init__(self):
        pass

    # Public

    def print_data(self, data):
        '''
        Вывод в терминал отсортированных данных.
        '''
        console = Console()

        table = Table(title=self.__TABLE_NAME)

        table.add_column("title", style="cyan", no_wrap=False)
        table.add_column("ctr", justify="right")
        table.add_column("retention_rate", justify="right")

        for row in data:
            table.add_row(*row)

        console.print(table)