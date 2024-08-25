name_list = {"Alice", "Bob"}


def get_name() -> str:
  name = input("What is your name? ")
  return name

def greet(name: str) -> None:
  print(f"Hello {name}!")

def is_authorised(name: str) -> bool:
  return name in name_list

def main():
  name = get_name()
  if is_authorised(name):
    greet(name)
  else:
    print("Sorry... You're not authorised to be greeted")
  return


if __name__ == "__main__":
  main()