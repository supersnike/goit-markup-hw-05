def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command. Usage: command args"
        except ValueError:
            return "Invalid input. Please enter valid arguments."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name or not phone:
        raise ValueError
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact_phone(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact '{name}' changed."
    else:
        raise KeyError

@input_error
def display_contact_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"Phone number for contact '{name}': {contacts[name]}"
    else:
        raise KeyError

def display_all_contacts(contacts):
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact_phone(args, contacts))
        elif command == "phone":
            print(display_contact_phone(args, contacts))
        elif command == "all":
            display_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
