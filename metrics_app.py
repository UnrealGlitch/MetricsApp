import argparse

from Helpers.data_loader import DataLoader
from Helpers.data_parser import DataParser
from Helpers.base_report import BaseReport
from Helpers.clickbait_report import ClickbaitReport

REPORTS: dict[str, BaseReport] = {
    "clickbait": ClickbaitReport(),
}

def __parse_args():
    '''
    Парсинг аргументов командной строки.
    Возвращение объекта с атрибутами files (список путей к CSV) и report (тип отчёта).
    '''
    parser = argparse.ArgumentParser(
        description="Анализ метрик из CSV файлов."
    )
    
    parser.add_argument(
        "--files",
        nargs="+",
        metavar="FILE",
        default=["Data/stats1.csv", "Data/stats2.csv"],
        help="Один или несколько CSV файлов со статистикой (например: stats1.csv stats2.csv)." \
        "По умолчанию будет выведен "
    )
    
    parser.add_argument(
        "--report",
        default="clickbait",
        choices=["clickbait"],
        help="Тип отчёта (например: clickbait)"
    )
    
    return parser.parse_args()

def main():
    '''
    Точка входа в приложение.
    Загруprf данных из CSV файлов, фильтрует, сортирует и вывод отчёта в терминал.
    '''
    args = __parse_args()
    report_name = args.report

    data_loader = DataLoader()
    data_parser = DataParser()
    report = REPORTS[report_name]

    loaded_files = [data_loader.load_data(file_path=file) for file in args.files]
    loaded_data = data_parser.combine_lists(*loaded_files)

    filtered_data = report.filter(loaded_data)
    sorted_data = report.sort(filtered_data)
    report.print_data(sorted_data)

if __name__ == "__main__":
    main()