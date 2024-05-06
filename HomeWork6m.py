from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if not self.valid_phone(phone):
             raise ValueError('Number must be 10 characters!')
        super().__init__(phone)

    def valid_phone(self, phone):
         return len(phone) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.list_phones = []

    def add_phone(self, phones):
        self.list_phones.append(Phone(phones))
        return self.list_phones
    
    def edit_phone(self, old_phone, new_phone):
        for num, phone in enumerate(self.list_phones):
            if phone == old_phone:
                if Phone.valid_phone(new_phone):
                    self.list_phones[num] = Phone(new_phone)
                    return new_phone
                else:
                    raise ValueError("New phone number is not valid.")
        raise ValueError("Phone number to edit not found.")

    def find_phone(self, phones):
        return print(self.phones.get(Phone(phones)))
    
    def delete_phone(self, phone_to_delete):
        for i, phone in enumerate(self.phones): 
            if phone.value == phone_to_delete:
                del self.phones[i]
                return phone_to_delete
        raise ValueError("Phone number to delete not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    phone = Phone() 
    def add_record(self, name):
        if name not in self.data:
            self.data[name] = Record(name)
            self.data[name].add_phone(AddressBook.phone)
        else:
            return f"Name is already in list!"

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found in the address book.")