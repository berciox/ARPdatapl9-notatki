contacts = {}
contacts["Aga"] = "13248184"
contacts["Kuba"] = "13251552"
# print(contacts.pop("Aga"))

def add_contacts (contacts, key, number):
    if key in contacts.keys():
        print("kontakt istnieje")
    else:
        contacts[key] = number
        print("dodano kontakt")

add_contacts(contacts, "Aga", "13248184")
add_contacts(contacts, "Arek", "13634684")