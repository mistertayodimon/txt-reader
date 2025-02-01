# txt-reader

Библиотека которая используется для чтения данных из txt-файлов.

## Установка

Для установки библиотеки вам необходимо использовать данную команду:
```bash
pip install git+https://github.com/mistertayodimon/txt-reader/
```
УСТАНАВЛИВАТЬ ТОЛЬКО ПО ЭТОЙ КОМАНДЕ !!!

Пример использования(после установки):
```bash
from txt_reader import read_file

content = read_file('ваш_файл.txt')
print(content)
```
ВАЖНО: Установите Git если он у вас не установлен.
Иначе будет вот такая ошибка:
Collecting git+https://github.com/mistertayodimon/txt-reader/ Cloning https://github.com/mistertayodimon/txt-reader/ to /data/data/ru.iiec.pydroid3/cache/pip-req-build-3ohugx1l ERROR: Error [Errno 2] No such file or directory: 'git' while executing command git version ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH? /storage/emulated/0 $
