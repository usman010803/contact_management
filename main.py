from tabulate import tabulate
contact_dict = {}


def add_contact():
    name = input("Enter contact name")
    number = input("Enter contact number")
    email = input("Enter contact email")

    contact_dict.update({name:(number,email)})


def view_contact():
    print(tabulate(contact_dict.items(), headers=["Contact Name", "Contact Details"]))


def search_contact():
    s_name = input("Enter name of contact that you want to search")
    if s_name in contact_dict:
        print("Contact is present in dictionary")
        print(contact_dict[s_name])

    else:
        print("Contact not present")


def delete_contact():
    d_name = input("Enter name of contact that you want to delete")
    contact_dict.pop(d_name)


def show_menu():
    print("Press 1 to add contact")
    print("Press 2 to view contact")
    print("Press 3 to search contact")
    print("Press 4 to delete contact")
    print("Press 5 to exit")


def main():
    show_menu()
    while True:
        choice = int(input("Enter your choice"))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

main()