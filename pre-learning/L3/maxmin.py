def maxmin(arr: list) -> list:
    top = -float("inf")
    bot = float("inf")

    for n in arr:
        if n > top:
            top = n
        if n < bot:
            bot = n

    return [bot, top]

def get_arr() -> list:
    string = input("Please enter your list in the format [n1, n2,... nm]: ")
    string = string[1:-1]
    str_arr = string.split(", ")
    int_arr = [int(x) for x in str_arr]
    return int_arr

def main():
    int_arr = get_arr()
    values = maxmin(int_arr)
    print(values)
    return

if __name__=="__main__":
    main()
