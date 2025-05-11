notebook = {
    "Raaj": 9816448727,
    "Tulsa": 9812977966,
    "Jagdev": 984455212
}

def display_menu():
    print("***Notebook menu***")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. list of all contact")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter a choice between 1 to 5: ")

    if choice == '1':
        name = input("Enter the contact: ")
        if name in notebook:
            print(f"{name} already exists")
        else:
            number = int(input("Enter a phone number: "))
            notebook[name] = number
            print(f"contact {name} added")

    elif choice == '2':
        name = input("Enter contact name to search: ")
        if name in notebook:
            print(f"{name}: {notebook[name]}")
        else:
            print("Contact not found")

    elif choice == '3':
        name = input("Enter a conact name you want to delete: ")
        if name not in notebook:
            print("contact name is not in notebook")
        else:
            del notebook[name]
            print(f"{name} is sucesfully deleted")

    elif choice == '4':
        if notebook:
            print("List of all contact is")
            for name, number in notebook.items():
                print(f"{name}: {number}")
        else:
            print("Contact not found")

    elif choice == '5':
        print("Thank you for using notebook! Bye")
        break

    else:
        print("Please enter a number between 1 to 5! thanks")



