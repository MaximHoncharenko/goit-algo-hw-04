data = [
    "60b90c1c13067a15887e1ae1,Tayson,3",
    "60b90c2413067a15887e1ae2,Vika,1",
    "60b90c2e13067a15887e1ae3,Barsik,2",
    "60b90c3b13067a15887e1ae4,Simon,12",
    "60b90c4613067a15887e1ae5,Tessi,5"
]

file_path = "cats_data.txt"

with open(file_path, "w") as file:
    for line in data:
        file.write(line + "\n")


def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r") as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print("Помилка при читанні файлу:", e)
    return cats_info

# Використання функції
cats_info = get_cats_info("cats_data.txt")
print(cats_info)