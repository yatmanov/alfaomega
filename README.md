# alfaomega

Для работы скрапера требуется python 3.6 и выше.

Установить зависимости в linux через 'pip3 install --user -r requirements.txt'

Запускать через 'python3 parser.py --output ./result.csv'

Можно задать задержку в секундах между запросами через необязательную опцию --delay командной строки.

#### Установка и запуск из виртуального окружения

Создать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

Установить зависимости:
```
pip3 install -r requirements.txt
```

Запустить скрипт:
```
python3 parser.py --output ./result.csv
```
