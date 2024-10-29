import game
from rich.table import Table

matrix = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
        ]


test_table = Table.grid()
for _ in range(3):
    test_table.add_column(width=1, no_wrap=True)
test_table.add_row("0", "1", "0")
test_table.add_row("1", "1", "1")
test_table.add_row("0", "1", "0")

def test_find_state():
    assert game.find_state(0, 0) == 0
    assert game.find_state(0, 1) == 0
    assert game.find_state(0, 2) == 0
    assert game.find_state(0, 3)== 1
    assert game.find_state(1, 0)== 0
    assert game.find_state(1, 2)== 1
    assert game.find_state(1, 4)== 0


def test_count_live_neighbours():
    assert game.count_live_neighbours(matrix, 0, 0) == 3
    assert game.count_live_neighbours(matrix, 1, 1) == 4
    assert game.count_live_neighbours(matrix, 2, 1) == 3


def test_update_source():
    assert game.update_source(matrix) == [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
            ]


def test_seed_read():
    with open("test.cells") as file:
        assert game.seed_read(file) == matrix
                

def test_generate_new_board():
    assert game.generate_new_board(matrix, 3, 3) == matrix

def test_check_seed():
    with open("test.cells") as test_file:
        assert game.check_seed(test_file, 3, 3) == True

def generate_dispaly():
    assert game.generate_display(matrix) == test_table


def test_init_game():
    assert game.init_game() == matrix
