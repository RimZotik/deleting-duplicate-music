import os
import re

def remove_mp3_duplicates():
    # Папка, где лежит этот скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Папка, где находятся mp3-файлы (родительская)
    target_dir = os.path.dirname(script_dir)

    # Регулярка: отрезает числовой ID в конце имени
    pattern = re.compile(r'^(.*)_\d+$', re.IGNORECASE)

    # Словарь: базовое имя -> оставленный файл
    seen = {}

    for filename in os.listdir(target_dir):
        if filename.lower().endswith(".mp3"):
            name_without_ext = os.path.splitext(filename)[0]
            match = pattern.match(name_without_ext)
            if match:
                base_name = match.group(1)
            else:
                base_name = name_without_ext

            full_path = os.path.join(target_dir, filename)

            if base_name not in seen:
                seen[base_name] = full_path
            else:
                # если файл с таким названием уже есть — удаляем дубликат
                print(f"Удаляю дубликат: {filename}")
                os.remove(full_path)

    print("✅ Проверка завершена. Дубликаты удалены.")

if __name__ == "__main__":
    remove_mp3_duplicates()
