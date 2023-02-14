import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone:
    contacts = []
    
    def load_contacts_from_csv(self):
        with open('/Users/brian/Repositories/python-cert/pcpp1_file_processing/contacts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def search_contacts(self, search_text):
        results = ''
        
        for contact in self.contacts:
            if contact.name.lower().find(search_text.lower()) != -1 or contact.phone.find(search_text) != -1:
                results += contact.name + ' (' + contact.phone + ')\n'
                
        if results == '':
            return 'No contacts found.'
        return results


new_phone = Phone()
new_phone.load_contacts_from_csv()
search_text = input('Search contacts: ')
print(new_phone.search_contacts(search_text))
