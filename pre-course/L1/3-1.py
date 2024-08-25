from sys import exit


def ask_user_for_number() -> int:
    n = input("Please enter an integer value here: ")
    if not n.isnumeric():
        exit("You did not enter an integer value.")
    return int(n)


def sum_to():
    n = ask_user_for_number()
    result = (n * (n + 1)) // 2
    return result


def sum_to_restricted():
    n = ask_user_for_number()
    result = 0
    for v in range(1, n+1):
        if not v % 3 or not v % 5:
            result += v
    return result


def factorial():
    n = ask_user_for_number()
    result = 1
    for v in range(1, n+1):
        result *= v
    return result

def main():
    option = input("""Welcome to limited calculator. Please select one of the following functions:\n
1. Sum to n\n
2. Sum of multiples of 3 and 5 to n\n
3. n!\n
Enter your selection here: """)
    if option in {"1", "2", "3"}:
        if option == "1":
            result = sum_to()
        elif option == "2":
            result = sum_to_restricted()
        else:
            result = factorial()
    else:
        result = "Please select a valid option."

    print(result)
    return


if __name__ == "__main__":
    main()