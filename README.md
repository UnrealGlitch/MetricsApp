# MetricsApp

hh.ru - https://ulyanovsk.hh.ru/resume/f3eab237ff105fc7030039ed1f6f4861393876

# == Запуск ==

Обязательно перейти в папку MetricsApp:

*cd MetricsApp*

Запуск файла через metrics_app.py:

Вариант по умолчанию (тестовые отчеты stats1 и stats2 будут взяты из папки Data, тип отчета будет clickbait):

*python3 metrics_app.py*

Вариант с несколькими своими входными метриками:

*python3 metrics_app.py --files Data/stats1.csv Data/stats2.csv Data/stats3.csv*

Вариант с указанием типа отчета:

*python3 metrics_app.py --files Data/stats1.csv Data/stats2.csv --report clickbait*

Вызвать помощь:

*python3 metrics_app.py --help*

# == Зависимости от библиотек ==

- csv
- tabulate
- argparse