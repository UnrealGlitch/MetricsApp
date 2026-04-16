from Helpers.data_loader import DataLoader
from Helpers.data_printer import DataPrinter
from Helpers.data_parser import DataParser

IS_TEST = True

def main():
    data_loader = DataLoader()
    data_parser = DataParser()

    loaded_data = []
    if IS_TEST:
        loaded_data1 = data_loader.load_test_data(file_number=1)
        loaded_data2 = data_loader.load_test_data(file_number=2)
        loaded_data = data_parser.combine_lists(loaded_data1, loaded_data2)

    filtered_data = data_parser.filter(loaded_data)

    data_printer = DataPrinter()
    data_printer.print_data(filtered_data)

if __name__ == "__main__":
    main()