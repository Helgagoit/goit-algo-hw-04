def total_salary(path):
    salaries = []
    total_salary = 0    # Змінна для зарплати
    count_dev = 0       # Змінна кількості розробників

    try:
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salary = float(salary)       
                    salaries.append((name, float(salary)))  
                    total_salary += salary  # Рахуємо зарплату 
                    count_dev += 1  # Рахуємо розробників
                except ValueError:
                    print(f'Невірний формат рядка: {line.strip()}')  # Обробка помилок форматування
        if count_dev == 0:  # Якщо немає записів
            print('Файл не містить жодного запису про зарплати')
            return 0, 0 

        average_salary = total_salary / count_dev  # Обчислюємо середню зарплату
        return total_salary, average_salary 

    except FileNotFoundError:   # якщо файл не існує
        print(f'Помилка: файл {path} не знайдено')
        return 0, 0
    except Exception as e:     #  обробка інших непередбачених помилок
        print(f'Невідома помилка при відкритті файлу: {e}')
        return 0, 0

# Приклад використання
total, average = total_salary('salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  