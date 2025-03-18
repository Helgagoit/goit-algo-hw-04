def get_cats_info(path):
    cats_info = []
    items = 0

    try:
        with open (path, 'r', encoding='utf-8') as file:
            for cat in file:
                try:
                     id, name, age = cat.strip().split(',')
                     cats_info.append({"id": id, "name": name, "age": int(age)})
                     items += 1              
                except ValueError:
                    print(f'Невірний формат рядка: {cat.strip()}')  # Обробка помилок форматування
        if items == 0:  # Якщо немає записів
            print('Файл не містить жодного запису про котів')
            return []  

    except FileNotFoundError:   # якщо файл не існує
        print(f'Помилка: файл {path} не знайдено')
        return []
    except Exception as e:     #  обробка інших непередбачених помилок
        print(f'Невідома помилка при відкритті файлу: {e}')
        return []
    return cats_info 
    
    # Приклад використання
cats_info = get_cats_info('Cats.txt')
print(cats_info)