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
Collecting git+https://github.com/mistertayodimon/txt-reader/ Cloning https://github.com/mistertayodimon/txt-reader/ to /data/data/ru.iiec.pydroid3/cache/pip-req-build-3ohugx1l ERROR: Error [Errno 2] No such file or directory: 'git' while executing command git version ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?

Вообще используйте Termux для использования библиотеки

Проверьте установлен ли у вас git при помощи команды git --version

Если Git установлен, вам покажут текущую версию, а если скажет команда не найдена установите Git прежде чем устанавливать библиотеку.

# Что выдает скрипт
Для начала вы должны установить библиотеку (это уже прописано выше)

Желательно создайте папку

Там сделайте txt файл

Пример: мы сделали txt "example.txt" со словом "hi"

Потом мы создаём скрипт (В примере показан)

ВАЖНО: Укажите имя вашего txt иначе ничего не получится!!!

Потом вам нужно прописать команду "python ваш_скрипт.py" (здесь будет имя вашего файла)

ВАЖНО: Если вы с Termux, проверьте установлен ли у вас Python 

Скрипт вам должен выдать:
hi

Если скрипт выдаст то что написано в txt значит все работает!

Удачи в использовании!
# Новые функции 
В версии 0.2.0 была добавлена функция читать все файлы разом 
Пример ее использования:
```bash
import txt_reader

# Читаем один файл
content = txt_reader.read_file("example.txt")
print(content)

# Читаем несколько файлов сразу
files_content = txt_reader.read_multiple_files("file1.txt", "file2.txt", "file3.txt")

for file, content in files_content.items():
    print(f"\nСодержимое {file}:\n{content}")
```
Вам нужно создать пять файлов

Первый файл: скрипт

Другие четыре файла: те самые txt

Скрипт должен будет выдать информацию которая хранится в этих файлах 

Удачи в использовании!

0.3.0

Новые функции!

Полный список изменений можно просмотреть во вкладке releases там выбираете 0.3.0

Примеры использования новых и старых функций библиотеки есть в txt файле

Удачи в использовании!
