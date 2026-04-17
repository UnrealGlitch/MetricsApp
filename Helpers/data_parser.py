if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataParser:
    '''
    Предварительный обработчик данных.
    Обединяет данные из входных файлов в один массив данных.
    '''

    # Life cycle

    def __init__(self):
        pass

    # Public functions

    def combine_lists(self, *args: list[list[str]]) -> list[list[str]]:
        '''
        Объединение неограниченного числа списков формата list[list[str]] в один.

        :param file_path: Путь к файлу.
        :return: Список list[list[str]] с заголовком в начале.
        '''
        result = []
        for i, lst in enumerate(args):
            if i == 0:
                result.extend(lst)
            else:
                result.extend(lst[1:])
        return result