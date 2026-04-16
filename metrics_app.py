from Helpers.data_loader import DataLoader
from Helpers.data_printer import DataPrinter

def main():
    data_loader = DataLoader()
    loaded_data = data_loader.load_test_data()

    data_printer = DataPrinter()
    data_printer.print_data(loaded_data)

if __name__ == "__main__":
    main()