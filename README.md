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
