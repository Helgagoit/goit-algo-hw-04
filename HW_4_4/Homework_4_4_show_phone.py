def show_phone(args, contacts):
    if not isinstance(args, list) or len(args) != 1:
        return "Error: Invalid input format. Provide exactly one name."
    name = args[0]
    if not isinstance(name, str) or not name.strip():
        return "Error: Name must be a non-empty string."
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    return contacts[name]


contacts = {"Olya": "00000000", "Nastya": "1111111111"}

print(show_phone(["Olya"], contacts)) 
