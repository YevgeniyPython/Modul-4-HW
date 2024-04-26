def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    if name in list(contacts.keys()):
        contacts[name] = phone
        return "Contact updated."
    else:
        return "There is no such name in the contact list"
    
def phone(args, contacts):
    name = args[0]
    if name in list(contacts.keys()):
        phone = contacts.get(name)
        return phone
    else:
        return "There is no such name in the contact list"   


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(contacts)
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()