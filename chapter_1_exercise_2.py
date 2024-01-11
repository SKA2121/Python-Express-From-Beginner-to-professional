# Exercise 2 : Managing a Dictionnary
address_books = {}

# Function to add a contact
def add_contact(name, number):
    address_books[name] = number

# delete a contact if it exists already in the dictionary
def delete_contact(name):
    if name in address_books:
        del address_books[name]

# display contacts
def display_contacts():
    for name, number in address_books.items():
        print(f"{name} : {number}")


# Calling the functions
add_contact("Alice", "555-1234")
add_contact("Bob", "555-5678")

display_contacts()

delete_contact("Bob")
display_contacts()
