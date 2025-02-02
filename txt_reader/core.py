VERSION = "txt_reader-0.3.0"

print(VERSION)  # Вывод версии перед выполнением любого скрипта

import os

def read_file(filename):
    """Читает содержимое одного TXT-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."

def read_multiple_files(*filenames):
    """Читает содержимое нескольких TXT-файлов."""
    content = {}
    for filename in filenames:
        content[filename] = read_file(filename)
    return content

def create_file(filename, content=""):
    """Создаёт новый TXT-файл и записывает в него данные."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Файл '{filename}' успешно создан.")

def edit_file(filename, new_content):
    """Редактирует существующий TXT-файл, заменяя его содержимое."""
    if os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Файл '{filename}' успешно отредактирован.")
    else:
        print(f"Ошибка: файл '{filename}' не найден.")

def delete_file(filename):
    """Удаляет указанный TXT-файл."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл '{filename}' успешно удалён.")
    else:
        print(f"Ошибка: файл '{filename}' не найден.")

def find_txt_files(directory="."):
    """Ищет все TXT-файлы в указанной директории."""
    txt_files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    if txt_files:
        print("Найденные TXT-файлы:")
        for file in txt_files:
            print(f"- {file}")
    else:
        print("TXT-файлы не найдены.")