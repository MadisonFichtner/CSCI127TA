# Contact represents a contact entity in a phone book
class Contact:
    def __init__(self, first, last, phone):
        self.first = first # first name
        self.last = last # last name
        self.phone = phone # full phone number: area_code-first_3_digits-last_4_digits
        self.title = '' # contact's title

    # get_area_code returns the area code of the phone number
    def get_area_code(self):
        return self.phone[0:3]

    # get_cell_number returns the full phone number for the contact
    def get_cell_number(self):
        return self.phone

    # print_entry pretty prints the contact's information
    def print_entry(self):
        name = ''
        if self.title != '': # only accomodate pretty printing of title if there is one
            name += self.title + ' '
        name += self.first + ' ' + self.last
        print('{:23}'.format(name), self.phone)

    # set_first_name modifies the contact's first name
    def set_first_name(self, first):
        self.first = first

    # set_title modifies the contact's title
    def set_title(self, title):
        self.title = title

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

main()
