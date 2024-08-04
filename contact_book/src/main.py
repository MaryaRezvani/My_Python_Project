from collections import defaultdict
from typing import Optional, Dict
from tabulate import tabulate
from termcolor import colored

class ContactBook:
    def __init__(self):
        # Store contacts in a dictionary
        self.contacts: Dict[str, Dict[str, Optional[str]]] = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: Optional[str] = None) -> None:
        """Add a new contact to the contact book"""
        if name in self.contacts:
            print(colored('Contact already exists!', 'red'))
            return
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email

    def view_contact(self) -> None:
        """Display all contacts in the contact book"""
        if not self.contacts:
            print(colored('No contacts found!', 'yellow'))
            return

        table_data = []
        for name, info in self.contacts.items():
            table_data.append([name, info['phone'], info['email']])

        headers = [colored('Name', 'blue'), colored('Phone', 'blue'), colored('Email', 'blue')]
        table = tabulate(table_data, headers=headers, tablefmt='fancy_grid')
        print(table)

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> None:
        """Update contact information for an existing contact"""
        if name in self.contacts:
            # Update phone and email with new values or keep existing ones
            self.contacts[name]['phone'] = phone if phone is not None else self.contacts[name].get('phone', '')
            self.contacts[name]['email'] = email if email is not None else self.contacts[name].get('email', '')
            print(colored('Contact updated successfully!', 'green'))
        else:
            print(colored('Contact not found!', 'red'))

    def delete_contact(self, name: str) -> None:
        """Delete a contact from the contact book"""
        if name in self.contacts:
            del self.contacts[name]
            print(colored("Contact deleted successfully!", 'green'))
        else:
            print(colored("Contact not found!", 'red'))

if __name__ == '__main__':
    book = ContactBook()

    while True:
        print('\n\nWelcome to contact book application!')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. View Contact')
        print('4. Delete Contact')
        print('5. Quit')

        user_choice = input('Please choose an option (1-5): ')
        if user_choice not in {'1', '2', '3', '4', '5'}:
            print(colored('Invalid choice! Please try again and choose a number between 1 and 5.', 'red'))
            continue

        if user_choice == '5':
            break
        
        elif user_choice == '1':
            name = input('\nEnter Contact name: ')
            phone = input('Enter Contact phone: ')
            email = input('Enter Contact email: ')

            book.add_contact(name, phone, email)

        elif user_choice == '2':
            name = input('\nEnter Contact name: ')
            phone = input('Enter Contact phone (leave blank if no change): ')
            email = input('Enter Contact email (leave blank if no change): ')

            # Update contact, handling empty phone or email inputs
            book.update_contact(name, phone if phone else '', email if email else '')

        elif user_choice == '3':
            print('\n\nList of Contacts: ')
            book.view_contact()

        elif user_choice == '4':
            name = input('\nEnter Contact name: ')
            book.delete_contact(name)

