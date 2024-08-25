animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"}
    #,{"name": "Poppet", "type": "Cow"}
]

def say_hello_to_pets(pets: list) -> None:
    for pet in pets:
        hello_message = ""
        pet_name = pet["name"]
        if pet["type"] == "dog":
            hello_message = "Woof"
        elif pet["type"] == "cat":
            hello_message = "Meow"
        else:
            raise TypeError
        print(f"{hello_message}, {pet_name}!")
    return


if __name__ == "__main__":
    say_hello_to_pets(animals)
