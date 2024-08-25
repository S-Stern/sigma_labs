from random import randint
from sys import exit


def start() -> None:
    print("""Welcome to Sigma Labs' number guessing game!
The game will randomly select a number between 1 and 1000.
You will then be able to guess the number.
The game will tell you if you are too low or too high, and allow you to guess again.
Good luck!""")

def game() -> tuple:
    ans = randint(1, 1000)
    last_guess = None
    guesses = 0
    win = False

    for i in range(1000):
        guess, is_valid = get_guess()
        if not is_valid:
            continue
        if guess == ans:
            win = True
            break
        bad_guess(ans, guess)
        if guess != last_guess:
            last_guess = guess
            guesses += 1

    return (win, guesses)


def get_guess() -> tuple:
    guess = input("Please enter your next guess here: ")
    try:
        return (int(guess), True)
    except:
        print("Please ensure your guess is an integer.")
        return (0, False)


def bad_guess(ans: int, guess: str) -> None:
    if guess < ans:
        print("Sorry, your guess was too low.")
    else:
        print("Sorry, your guess was too high.")
    return


def end(res: tuple) -> None:
    if res[0]:
        print(f"Congratulations! You won with {res[1]} guesses.")
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
