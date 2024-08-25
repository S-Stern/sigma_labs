from random import randrange


def reverse_name(name: str) -> str:
  return name[::-1]


def intersperse_name(name1: str, name2: str) -> str:
  i = 0
  interspersed = ""
  
  while name1[i:i+1] and name2[i:i+1]:
    interspersed += name1[i] + name2[i]
    i += 1
    
  if name1[i:]:
    return interspersed + name1[i:]
  elif name2[i:]:
    return interspersed + name2[i:]
  return interspersed


def format_name(name: str) -> str:
  mid = len(name) // 2
  name1 = name[0:1].upper() + name[1:mid].lower()
  name2 = name[mid:mid+1].upper() + name[mid+1:].lower()
  return name1 + " " + name2
  

def option1():
  name1 = input("Enter your first name here: ")
  name1_r = reverse_name(name1)
  name2 = input("Enter your surname name here: ")
  int_name = intersperse_name(name1_r, name2)
  print(format_name(int_name))
  return


def random_string(length: int) -> str:
  random_str = ""
  for i in range(length):
    random_str += chr(randrange(33, 126))
  return random_str


def option2():
  username = str(" ".join([rand_str(5) for i in range(2)]))
  print(f"Your random username is: {username}")
  return


def main():
  option = input("""Welcome to the username creator... Please choose one of the following options:\n
1. Create a username based on a name\n
2. Create a random username\n
Enter your choice here: """)
  if option not in {"1", "2"}:
    print("You must select an option")
  elif option == "1":
    option1()
  else:
    option2()
  return


if __name__ == "__main__":
  main()