def add_contact(args, contacts):
    if not isinstance(args, list) or len(args) != 2:
        return "Error: Invalid input format. Provide name and phone."
    name, phone = args 
    if not isinstance(name, str) or not name.strip():
        return "Error: Name must be a non-empty string."
    if not isinstance(phone, str) or not phone.isdigit():
        return "Error: Phone number must contain only digits."
    contacts[name] = phone
    return f"Contact '{name}' added successfully."

contacts = {}


print(add_contact(["Olya", "123456789"], contacts))
print(contacts) 