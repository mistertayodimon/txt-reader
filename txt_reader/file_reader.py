VERSION = "txt_reader-0.2.0"

print(VERSION)  # Вывод версии перед выполнением любого скрипта

def read_file(file_path):
    """Читает содержимое одного файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Ошибка при чтении {file_path}: {e}"

def read_multiple_files(*file_paths):
    """Читает содержимое нескольких файлов и возвращает их в виде словаря"""
    result = {}
    for path in file_paths:
        result[path] = read_file(path)
    return result
