from rich.console import Console
from rich.table import Table

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
        console = Console()

        table = Table(title=self.report_name)

        table.add_column("title", style="cyan", no_wrap=False)
        table.add_column("ctr", justify="right")
        table.add_column("retention_rate", justify="right")

        for i in range(1, len(data)):
            table.add_row(*data[i])

        console.print(table)