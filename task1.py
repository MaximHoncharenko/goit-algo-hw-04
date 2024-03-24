# Вміст файлу
file_content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

# Записуємо вміст у файл
with open("salary_file.txt", "w", encoding="utf-8") as file:
    file.write(file_content)

print("Файл успішно створено.")


def total_salary(path):
    total = 0
    count = 0
    
    try:
        # Відкриваємо файл для зчитування
        with open(path, "r", encoding="utf-8") as file:
            # Проходимо по кожному рядку у файлі
            for line in file:
                # Розділяємо рядок за комами
                parts = line.strip().split(',')
                # Перший елемент - ім'я розробника, другий - його заробітна плата
                salary = int(parts[1])
                total += salary
                count += 1
        
        # Обчислюємо середню зарплату
        average = total / count if count > 0 else 0
        
        # Повертаємо кортеж із загальною сумою зарплати та середньою заробітною платою
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print("Сталася помилка при обробці файлу:", e)
        return None, None

# Викликаємо функцію total_salary зі шляхом до файлу
total, average = total_salary("salary_file.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
