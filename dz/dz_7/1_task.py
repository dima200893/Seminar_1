import os


def group_rename(desired_name, num_digits, source_ext, target_ext, name_range=None):
    # Получаем список всех файлов в текущем каталоге
    files = [f.split(source_ext)[0] for f in os.listdir('.')
             if os.path.isfile(f) and f.endswith(source_ext)]

    # Проверяем, что файлы присутствуют
    if not files:
        print("Файлы с заданным расширением не найдены.")
        return

    # Перебираем файлы и переименовываем их
    for i, file in enumerate(files, 1):
        # Извлекаем часть имени в соответствии с диапазоном
        if name_range:
            start, end = name_range
            base_name = file[start - 1:end]

        # Собираем новое имя файла
        new_name = base_name + desired_name + f"{i:0{num_digits}}" + target_ext

        # Переименовываем файл
        os.rename(f'{file}{source_ext}', new_name)
        print(f"Переименован файл {file} в {new_name}")


group_rename("_new", 6, ".txt", ".doc", name_range=[3, 6])