
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()  
    else:
        return "No contacts found." 
    

contacts = {"Olya": "00000000", "Nastya": "1111111111"}

print(show_all(contacts))



    # if not isinstance(args, list) or len(args) > 0:
    #     return "Error: This command does not require any arguments."

    # # Перевіряємо, чи є контакти в словнику
    # if not contacts:
    #     return "No contacts found."

    # # Форматуємо список контактів
    # result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    # return result
    #print(show_all([], contacts))