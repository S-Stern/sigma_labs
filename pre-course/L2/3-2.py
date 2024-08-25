#I know there's no validation here, but it wasn't in the task.


def print_all(people_dict: dict) -> None:
    for person in people_dict:
        print(f"Name: {person}")
        print(f"Age: {people_dict[person]["age"]}")
        print(f"Employed: {people_dict[person]["employed"]}")
    
    return


def prompt(people_dict: dict) -> dict:
    choice = input("What action would you like to perform? (Add/Remove)")
    if choice == "Add":
        add_person(people_dict)
    elif choice == "Remove":
        remove_person(people_dict)


def add_person(people_dict: dict) -> None:
    name = input("Name: ")
    age = input("Age: ")
    employed = input("Employed: ")
    people_dict[name] = {"Age": age, "Employed": employed}
    return people_dict


def remove_person(people_dict: dict) -> None:
    name = input("Please enter the name here: ")
    try: 
        del people_dict[name]
    except:
        print("Name not recognised.")
    return people_dict


def main():
    people = {"Jane Doe" : {"age": 42, "employed": True},
        "Tom Smith": {"age": 18, "employed": True}, 
        "Mariam Coulter": {"age": 66, "employed": False}, 
        "Gregory Tims": {"age": 8, "employed": False}}
    # I wouldn't usually do this, but 6 seemed to imply you didn't want the 
    # program to terminate. Use keyboard interrupt if desired.
    while True:
        people = prompt(people)
        print_all(people)
    return


if __name__ == "__main__":
    main()
        