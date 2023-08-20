class FamilyMember:
    def background_info(self, name, birthdate, gender):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.parent = None
        self.spouse = None
        self.children = []

def add_child(parent, child):
    parent.children.append(child)
    child.parent = parent

def add_spouse(person1, person2):
    person1.spouse = person2
    person2.spouse = person1

def display_family_tree(person, generation=0):
    indentation = "    " * generation
    spouse_info = ""
    if person.spouse:
        spouse_info = f" --- (Spouse: {person.spouse.name} - Born: {person.spouse.birthdate.split('-')[0]})"
    print(f"{indentation}!-->{person.name} ({person.gender}) - Born: {person.birthdate.split('-')[0]}{spouse_info}")

    for child in person.children:
        display_family_tree(child, generation + 1)


def create_family_member():
    name = input("Enter the name: ")
    birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
    gender = input("Enter the gender (Male/Female): ")
    return FamilyMember(name, birthdate, gender)

def main():
    print("Welcome to the Family Tree Program!")

    root = create_family_member()

    while True:
        print("\nMenu:")
        print("1. Add a child")
        print("2. Add a spouse")
        print("3. Display family tree")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            child = create_family_member()
            add_child(root, child)
            print(f"{child.name} added as a child of {root.name}.")
        elif choice == "2":
            spouse = create_family_member()
            add_spouse(root, spouse)
            print(f"{spouse.name} added as the spouse of {root.name}.")
        elif choice == "3":
            print("\nFamily Tree:")
            display_family_tree(root)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please re-enter choice correctly.")

if __name__ == "__main__":
    main()
