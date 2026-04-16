if __name__ == "__main__":
    raise Exception("Нужно запускать metrics_app.py")

class DataParser:
    '''
    Обработчик данных.
    '''

    # Life cycle

    def __init__(self):
        pass

    # Public functions

    def combine_lists(self, *args: list[list[str]]) -> list[list[str]]:
        '''
        Объединить неограниченное число списков формата list[str] в один.
        '''
        result = []
        for i, lst in enumerate(args):
            if i == 0:
                result.extend(lst)
            else:
                result.extend(lst[1:])
        return result

    def filter(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Фильтрация данных по критериям ctr > 15 и retention_rate < 40. 
        Возвращает отфлитрованный список list[str].
        '''
        output_list = []
        ctr_index, retention_rate_index = self.__get_headers_indexies(data[0])
        for i in range(1, len(data)):
            row = data[i]
            if float(row[ctr_index]) > 15 and float(row[retention_rate_index]) < 40:
                output_list.append(row)
        return [data[0]] + output_list
    
    def sort(self, data: list[list[str]]) -> list[list[str]]:
        '''
        Сортировка данных по убыванию по полю ctr.
        '''
        if len(data) == 0:
            return data
        
        ctr_index, _ = self.__get_headers_indexies(data[0])

        header = data[0]
        rows = data[1:]
        
        sorted_rows = sorted(rows, key=lambda x: float(x[ctr_index]), reverse=True)
        
        return [header] + sorted_rows
    
    # Private functions

    def __get_headers_indexies(self, headers: list[list[str]]):
        ctr_index = -1
        retention_rate_index = -1
        for i in range(len(headers)):
            if headers[i] == "ctr":
                ctr_index = i
            elif headers[i] == "retention_rate":
                retention_rate_index = i
        return (ctr_index, retention_rate_index)