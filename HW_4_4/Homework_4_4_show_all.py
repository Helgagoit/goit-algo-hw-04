
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()  
    else:
        return "No contacts found." 
    

# contacts = {"Olya": "00000000", "Nastya": "1111111111"}

# print(show_all(contacts))