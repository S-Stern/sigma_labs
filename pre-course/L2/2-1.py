from random import randint
from sys import exit


def game() -> tuple:
    ans = randint
    last_guess = -float("inf")
    guesses = 0
    win = False

    for i in range(1000):
        guess = input("Please enter your next guess here: ")
        if guess == ans:
            win = True
            break
        if guess != last_guess:
            last_guess = guess
            guesses += 1
        if guess < ans:
            print("Sorry, your guess was too low.")
        print("Sorry, your guess was too high.")

    return (win, guesses)


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
