import argparse

from Helpers.data_loader import DataLoader
from Helpers.data_printer import DataPrinter
from Helpers.data_parser import DataParser

def __parse_args():
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
    args = __parse_args()
    files = args.files
    report_name = args.report

    data_loader = DataLoader()
    data_parser = DataParser()

    loaded_files = []
    for file in files:
        loaded_files.append(data_loader.load_data(file_path=file))
    loaded_data = data_parser.combine_lists(*loaded_files)

    filtered_data = data_parser.filter(loaded_data)
    sorted_data = data_parser.sort(filtered_data)

    data_printer = DataPrinter(report_name=report_name)
    data_printer.print_data(sorted_data)

if __name__ == "__main__":
    main()