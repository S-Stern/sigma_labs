from sys import argv, exit
from typing import TextIO
from rich.live import Live
from rich.table import Table
from time import sleep

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


def get_config() -> dict:
    config_dict = {"display-height": 30, "dispaly-width": 30, "refresh-rate": 1, "seed": None}
    with open(config) as config:
        for line in config:
            components = line.split(": ")
            config_dict[components[0]] = components[1]
    return config_dict


def seed_read(file: list) -> list:
    seed = []
    for line in file:
        to_append = [int(x == "O") for x in line]
        seed.append(to_append)
    return seed


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

def check_seed(file: list, height: int, width: int) -> bool:
    seed_width = 0
    seed_height = 0
    for line in file:
        seed_width = max(len(line), seed_width)
        seed_height += 1
    return not (seed_height > height or seed_width > width)


def generate_display(board: list) -> Table:
    table = Table.grid()
    for _ in range(len(board[0])):
        table.add_column(width=1, no_wrap=True)
    for row in board:
        table.add_row(*["0" if x else " " for x in row])
    return table


def cells_to_list(file: str) -> list:
    as_list = []
    with open(file) as to_read:
        as_list = [line for line in to_read if not line.startswith("!")]
    for i, line in enumerate(as_list):
        as_list[i] = line[:-2]
    return as_list

def init_game(args: list) -> list:
    board_height = 0
    board_width = 0
    mode = len(args) - 1
    if mode == 1:
        board_height = 30
        board_width = 30
    elif mode == 3:
        board_height = int(args[2])
        board_width = int(args[3])
    else:
        exit("Illegal number of arguments. Please check proper usage.")

    if not args[1].endswith(".cells"):
        exit("Illegal seed. Please check proper usage.")
    
    seed_file = cells_to_list(argv[1])
    legal_seed = check_seed(seed_file, board_height, board_width)
    seed = seed_read(seed_file)

    if not legal_seed:
        proceed = input("""Seed size exceeds display size and will be truncated.
        Do you wish to proceed? (Y/n) """)
        if not proceed == "Y":
            exit()
    return generate_new_board(seed, board_height, board_width)


def run_game(board: list) -> None:
    display = generate_display(board)

    with Live(display, auto_refresh=False, screen=True) as live:
        for _ in range(10000):
            sleep(0.05)
            board = update_source(board)
            display = generate_display(board)
            live.update(display, refresh=True)


def main():
    board = init_game(argv)
    run_game(board)
    return


if __name__ == "__main__":
    main()
