from sys import argv, exit
from typing import TextIO
from rich import print, box
from rich.live import Live
from rich.table import Table
from rich.console import Group
from rich.prompt import Prompt
import re
from time import sleep



def init_game() -> list:
    config_dict = get_config()
    seed_file = config_dict["seed"]
    board_height = config_dict["display-height"]
    board_width = config_dict["display-width"]
    refresh_rate = config_dict["refresh-rate"]
    try:
        seed_file = cells_to_list(config_dict["seed"])
        legal_seed = check_seed(seed_file, board_height, board_width)
        seed = seed_read(seed_file)
    except FileNotFoundError:
        print("[bold red]Warning: selected seed could not be loaded; board defaulted to 10cellinfinitegrowth[/bold red]")
        seed = seed_read('10cellinfinitegrowth.cells')
        print(seed)
    board = generate_new_board(seed, board_height, board_width)
    return board, refresh_rate



def get_config() -> dict:
    config_dict = {"display-height": 30, "display-width": 30, "refresh-rate": 1, "seed": None}
    with open("config") as config:
        for line in config:
            components = line.split(": ")
            config_dict[components[0].strip()] = components[1].strip()
    seed = []
    legal_seed = True
    board_height = config_dict["display-height"]
    board_width = config_dict["display-width"]

    if not board_height.isnumeric():
        print("[bold red]Warning: selected height was not an integer value; value set to default (30)[/bold red]")
        config_dict["display-height"] = 30
    else:
        config_dict["display-height"] = int(board_height)

    if not board_width.isnumeric():
        print("[bold red]Warning: selected width was not a positive integer; value set to default (30)[/bold red]")
        config_dict["display-width"] = 30
    else:
        config_dict["display-width"] = int(board_width)

    if not re.match(r'(\d+(?:\.\d+)?)', config_dict["refresh-rate"]):
        print("[bold red]Warning: selected refresh rate was not a positive decimal number; value set to default (1)[/bold red]")
        config_dict["refresh-rate"] = 1.0
    else:
        config_dict["refresh-rate"] = float(config_dict["refresh-rate"])

    return config_dict



def cells_to_list(file: str) -> list:
    as_list = []
    print(file)
    with open(file) as to_print:
        print(file)
    with open(file) as to_read:
        as_list = [line for line in to_read if not line.startswith("!")]
    for i, line in enumerate(as_list):
        as_list[i] = line[:-2]
    print(file)
    print(as_list)
    return as_list



def check_seed(file: list, height: int, width: int) -> bool:
    seed_width = 0
    seed_height = 0
    for line in file:
        seed_width = max(len(line), seed_width)
        seed_height += 1
    return not (seed_height > height or seed_width > width)



def seed_read(file: list) -> list:
    seed = []
    for line in file:
        to_append = [int(x == "O") for x in line]
        seed.append(to_append)
    return seed


def find_state(cell: int, score: int) -> int:
    return int((score == 3) or (cell and score == 2))



def count_live_neighbours(matrix: list, row: int, col: int) -> int:
    height = len(matrix)
    width = len(matrix[0])
    return sum([
            matrix[i][j]
            if (i, j) != (row, col) and 0 <= i < height and 0 <= j < width
            else 0
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            ])


def update_source(board: list) -> list:
    height = len(board)
    width = len(board[0])
    new_grid = [[0 for _ in range(width)] for _ in range(height)]

    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            score = count_live_neighbours(board, r, c)
            state = find_state(cell, score)
            new_grid[r][c] = state

    return new_grid


def generate_new_board(seed: list, height: int, width: int) -> list:
    new_board = []
    for x in range(height):
        new_row = []
        if seed[x:x+1]:
            new_row += seed[x][:width]
        diff = width - len(new_row)
        if diff > 0:
            new_row += [0 for _ in range(diff)]
        new_board.append(new_row)
    return new_board


def generate_display(board: list) -> Table:
    table = Table.grid()
    for _ in range(len(board[0])):
        table.add_column(width=1, no_wrap=True)
    for row in board:
        table.add_row(*["0" if x else " " for x in row])
    return table


def generate_info_pannel(generation: int, living: int) -> Table:
    display = Table(box=box.ROUNDED, show_header=False)
    display.add_column()
    display.add_row("Generation: ", str(generation))
    display.add_row("Population: ", str(living))
    return display


def run_game(generation: int, board: list, refresh: float) -> tuple:

    sleep(1/refresh)
    new_board = update_source(board) 
    display = generate_display(new_board)
    info_pannel = generate_info_pannel(generation, sum([sum(row) for row in new_board]))
    total_display = Group(display, info_pannel)
    generation += 1
    return total_display, generation, new_board, refresh


def display_game(board: list, refresh = float):
    display = generate_display(board)

    with Live(display, auto_refresh=False, screen=True) as live:
        edit = False
        generation = 0
        for _ in range(10000):
            display, generation, board, refresh = run_game(generation, board, refresh)
            live.update(display, refresh=True)
    print('Thank you for playing. The game has now ended.')
    return


def main():
    board, refresh = init_game()
    display_game(board, refresh)
    return


if __name__ == "__main__":
    main()
