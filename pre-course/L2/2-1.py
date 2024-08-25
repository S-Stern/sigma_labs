from random import randint
from sys import exit


def game() -> tuple:
    ans = randint
    last_guess = float("inf")
    guesses = 0
    win = False

    for i in range(1000):
        guess = get_guess()
        if not type(guess) == int:
            break
        if guess == ans:
            win = True
            break
        if guess != last_guess:
            last_guess = guess
            guesses += 1

    exit("Apologies; you exceeded the guess limit and the program terminated.")


def get_guess() -> tuple:
    guess = input("Please enter your next guess here: ")
    try:
        return int(guess)
    except:
        print("Please ensure your guess is an integer.")
        return guess


def bad_guess(ans: int, guess: str) -> None:
    if guess < ans:
        print("Sorry, your guess was too low.")
    else:
        print("Sorry, your guess was too high.")
    return


def start() -> None:
    print("Welcome to Sigma Labs' number guessing game!")


def end(res: tuple) -> None:
    if res[0]:
        print(f"Congratulations! You won with {tuple[1]} guesses.")
    else:
        print("Apologies; you exceeded the maximum of 1000 guesses and the program terminated.")
    return


def main():
    start()
    results = game()
    end(results)
    return


if __name__ == "__main__":
    main()
