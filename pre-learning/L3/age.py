from datetime import datetime, date
from re import match
from sys import exit

def answer(years: int) -> None:
    print(f"A person born on that date would now be {years}")


def years_from(string: str) -> int:
    day, month, year = [int(x) for x in string.split("-")]
    try:
        prev = date(year, month, day)
    except:
        exit("Date not recognised")
    curr = date.today()
    diff = curr - prev
    diff_years = diff.days // 365
    return diff_years


def get_str() -> str:
    attempt = input("Please input your birthday in the dd-mm-yyyy format: ")
    if not match('^[0-9]{2}-[0-9]{2}-[0-9]{4}$', attempt):
       exit("Date inputted in incorrect format")
    return attempt


def main():
    answer(years_from(get_str()))


if __name__=="__main__":
    main()
