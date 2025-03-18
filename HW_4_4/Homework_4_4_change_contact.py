def change_contact(args, contacts):
    if not isinstance(args, list) or len(args) != 2:
        return "Error: Invalid input format. Provide name and new phone number."
    name, new_phone = args  
    if not isinstance(name, str) or not name.strip():
        return "Error: Name must be a non-empty string."
    if not isinstance(new_phone, str) or not new_phone.isdigit():
        return "Error: Phone number must contain only digits."
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    contacts[name] = new_phone
    return f"Contact '{name}' updated successfully."

contacts = {"Olya": "00000000", "Nastya": "1111111111"}

print(change_contact(["Olya", "19999999"], contacts)) 
print(contacts) 