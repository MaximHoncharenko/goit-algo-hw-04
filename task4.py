def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return None, None  # Якщо не вдалося розібрати введення, повертаємо None

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid arguments for adding a contact."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            with open("contacts.txt", "a+") as file:  # Відкриваємо файл для додавання або читання
                user_input = input("Enter a command: ")
                command, *args = parse_input(user_input)

                if command in ["close", "exit"]:
                    print("Good bye!")
                    break
                elif command == "hello":
                    print("How can I help you?")
                elif command == "add":
                    print(add_contact(args, contacts))
                    # Додаємо контакт до файлу
                    file.write(f"{args[0]},{args[1]}\n")
                else:
                    print("Invalid command.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
