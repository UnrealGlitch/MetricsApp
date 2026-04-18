import os
import tempfile
import pytest

from Helpers.data_loader import DataLoader
from Helpers.data_parser import DataParser
from Helpers.clickbait_report import ClickbaitReport

# Fixtures

@pytest.fixture
def data_loader():
    return DataLoader()

@pytest.fixture
def data_parser():
    return DataParser()

@pytest.fixture
def report():
    return ClickbaitReport()

@pytest.fixture
def sample_data():
    '''
    Входные данные.
    '''
    return [
        ["title", "ctr", "retention_rate", "views"],
        ["Заголовок A", "25", "22", "10000"],
        ["Заголовок B", "10", "15", "5000"],
        ["Заголовок C", "20", "45", "8000"],
        ["Заголовок D", "18", "30", "7000"],
        ["Заголовок E", "22", "25", "9000"],
    ]

@pytest.fixture
def filtered_data():
    '''
    Данные после фильтрации — только нужные колонки и строки.
    '''
    return [
        ["title", "ctr", "retention_rate"],
        ["Заголовок A", "25", "22"],
        ["Заголовок D", "18", "30"],
        ["Заголовок E", "22", "25"],
    ]

# DataLoader

class TestDataLoader:

    def test_load_data_file_not_found(self, data_loader):
        '''
        FileNotFoundError при несуществующем файле.
        '''
        with pytest.raises(FileNotFoundError):
            data_loader.load_data(file_path="test_file_not_found.csv")
        
    def test_load_data_empty_file(self, data_loader):
        '''
        Пустой файл возвращает пустой список.
        '''
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as file:
            path = file.name
        try:
            result = data_loader.load_data(file_path=path)
            assert result == []
        finally:
            os.unlink(path)

# DataParser

class TestDataParser:

    def test_combine_lists(self, data_parser):
        '''
        При объединении двух списков заголовок присутствует только один раз.
        '''
        list1 = [["title", "ctr"], ["A", "10"]]
        list2 = [["title", "ctr"], ["B", "20"]]
        result = data_parser.combine_lists(list1, list2)
        headers = [row for row in result if row == ["title", "ctr"]]
        assert len(headers) == 1

# ClickbaitReport

class TestClickbaitReport:

    def test_filter_removes_low_ctr(self, report, sample_data):
        '''
        Строки с ctr <= 15 отфильтровываются.
        '''
        result = report.filter(sample_data)
        ctrs = [float(row[1]) for row in result[1:]]
        assert all(ctr > 15 for ctr in ctrs)

    def test_filter_removes_high_retention(self, report, sample_data):
        '''
        Строки с retention_rate >= 40 отфильтровываются.
        '''
        result = report.filter(sample_data)
        retentions = [float(row[2]) for row in result[1:]]
        assert all(r < 40 for r in retentions)

    def test_sort_descending_by_ctr(self, report, filtered_data):
        '''
        Строки отсортированы по убыванию ctr.
        '''
        result = report.sort(filtered_data)
        ctrs = [float(row[1]) for row in result[1:]]
        assert ctrs == sorted(ctrs, reverse=True)