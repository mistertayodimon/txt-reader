def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Ошибка: {e}"
