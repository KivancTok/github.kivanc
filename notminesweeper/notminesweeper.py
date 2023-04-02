import math
import os
import time

import arr2D
import random


def minesweeper():
    hit_mine = False
    has_won = False
    all_mine = bool(random.choice([0] * 199 + [1]))
    board_width = int(input('Columns: '))
    col_digits = math.floor(math.log10(board_width)) + 1
    board_height = int(input('Rows: '))
    row_digits = math.floor(math.log10(board_height)) + 1
    mines_to_place = int(input(f'Mines to place (max. {(board_width - 1) * (board_height - 1)}): '))
    mines_to_place = mines_to_place if mines_to_place <= (board_width - 1) * (board_height - 1) else (board_width - 1) * (board_height - 1)

    hm_pos = (0, 0)

    mines_to_place = mines_to_place if 0 < mines_to_place else 1
    mines_left = mines_to_place
    discovered_left = board_height * board_width - mines_to_place

    board = arr2D.Array2D.zero(board_height, board_width, 'Notminesweeper Board')
    is_mine = arr2D.Array2D.false(board_height, board_width, 'Mine cells')
    flagged = arr2D.Array2D.false(board_height, board_width, 'Flagged cells')
    is_potential = arr2D.Array2D.false(board_height, board_width, 'Potentially mines')
    discovered = arr2D.Array2D.false(board_height, board_width, 'Discovered cells')
    mines_around = arr2D.Array2D.zero(board_height, board_width, 'Mines around a cell')

    turns = 1

    if all_mine:
        for i in range(board_height):
            for j in range(board_width):
                is_mine[i, j] = True

    else:
        while mines_to_place > 0:
            board_row = random.randint(0, board_height - 1)
            board_col = random.randint(0, board_width - 1)
            if not is_mine[board_row, board_col]:
                is_mine[board_row, board_col] = True
                mines_to_place -= 1

    for i in range(board_height):
        for j in range(board_width):
            neighbors = is_mine.get_neighbors(1, 1, i, j)

            mine_neighbors = 0
            for k in range(neighbors.rows):
                for m in range(neighbors.cols):
                    mine_neighbors += int(neighbors[k, m])

            mine_neighbors -= board[i, j]

            mines_around[i, j] = (neighbors.rows * neighbors.cols - 1) - mine_neighbors

    os.system('cls')

    while not (hit_mine or has_won):
        os.system('cls')

        print('''Hi! this is Notminesweeper. Here, you don\'t see how many mines there are, but how many mines there aren\'t. Have fun!
When Playing
-: Not marked
Number: Discovered cell (not a mine) - Use d for discover to discover a cell. You cannot discover a flagged cell.
F: Flag (a mine) - Use f for flag to flag a cell. If a cell is flagged twice, the flag will get removed. You cannot flag a discovered cell.
P: Potentially a mine - Use p for potential mine to mark a cell potentially a mine. If a cell is marked with this twice, it will get removed.
   Discovering or flagging will get the marker removed.
--------------------------------------------------------------------------------------------------------------------------------------------------
When Hit Mine
-: Not marked
Number: Discovered cell - The cell has been discovered.
H: The mine you hit.
M: Other mine - A mine you didn't hit.
F: True positive flag - Flag put on a mine.
f: False positive flag - Flag not put on a mine.
P: True guess - Potential mine marker put on a mine.
p: False guess - Potential mine marker not put on a mine.
--------------------------------------------------------------------------------------------------------------------------------------------------''')

        print(f'Mines left: {mines_left} - Turn {turns}')

        print(end=' ' * row_digits)
        for i in range(mines_around.cols):
            print(end=' ')
            print(end=f'{i + 1:<{col_digits}}')

        print()

        for i in range(mines_around.rows):
            print(f'{i + 1:>{row_digits}}', end=' ')
            for j in range(mines_around.cols):
                if discovered[i, j]:
                    print(mines_around[i, j], end='')

                elif flagged[i, j]:
                    print('F', end='')

                elif is_potential[i, j]:
                    print('P', end='')

                else:
                    print('-', end='')

                if j < mines_around.cols - 1:
                    print(end=' ' * col_digits)

            print()

        fd = input('[F]lag - [D]iscover - [P]otential Mine? ')

        if fd.lower() == 'd':
            dp = input('Row, column to discover (leave 1 space between row and column, C to cancel): ')

            if dp.lower() == 'c':
                continue

            dp = dp.split()
            try:
                row = int(dp[0]) - 1
                col = int(dp[1]) - 1

                if is_mine[row, col]:
                    hit_mine = True
                    hm_pos = (row, col)
                    continue

                if hit_mine and turns == 1:
                    if not all_mine:
                        hit_mine = False
                        is_mine[row, col] = False

                        board_row, board_col = 0, 0

                        while not is_mine[board_row, board_col] and board_row != row and board_col != col:
                            board_row = random.randint(0, board_height - 1)
                            board_col = random.randint(0, board_width - 1)
                            if not is_mine[board_row, board_col] and board_row != row and board_col != col:
                                is_mine[board_row, board_col] = True

                discovered[row, col] = not flagged[row, col]

                if is_potential[row, col]:
                    is_potential[row, col] = False

                discovered_left -= 1

            except Exception:
                pass

        elif fd.lower() == 'f':
            fp = input('Row, column to flag (leave a space between row and column, C to cancel): ')

            if fp.lower() == 'c':
                continue

            fp = fp.split()

            try:
                flagged[int(fp[0]) - 1, int(fp[1]) - 1] = not flagged[int(fp[0]) - 1, int(fp[1]) - 1] and not discovered[int(fp[0]) - 1, int(fp[1]) - 1]

                if flagged[int(fp[0]) - 1, int(fp[1]) - 1]:
                    if is_potential[int(fp[0]) - 1, int(fp[1]) - 1]:
                        is_potential[int(fp[0]) - 1, int(fp[1]) - 1] = False
                    mines_left -= 1

                else:
                    mines_left += 1

            except Exception:
                pass
        elif fd.lower() == 'p':
            pp = input('Row, column to put a potential marker (leave a space between row and column, C to cancel): ')

            if pp.lower() == 'c':
                continue

            pp = pp.split()

            try:
                is_potential[int(pp[0]) - 1, int(pp[1]) - 1] = not (is_potential[int(pp[0]) - 1, int(pp[1]) - 1]) and not (flagged[int(pp[0]) - 1, int(pp[1]) - 1] or discovered[int(pp[0]) - 1, int(pp[1]) - 1])

            except Exception:
                pass

        turns += 1

        has_won = mines_left == 0 and discovered_left == 0

    if hit_mine:
        print('You hit a mine! :(')

        print(end=' ' * row_digits)
        for i in range(mines_around.cols):
            print(end=' ')
            print(end=f'{i + 1:<{col_digits}}')

        print()

        for i in range(board_height):
            print(f'{i + 1:>{row_digits}}', end=' ')
            for j in range(mines_around.cols):
                if is_mine[i, j] and flagged[i, j]:
                    print('F', end='')

                elif not is_mine[i, j] and flagged[i, j]:
                    print('f', end='')

                elif is_mine[i, j] and is_potential[i, j]:
                    print('P', end='')

                elif not is_mine[i, j] and is_potential[i, j]:
                    print('p', end='')

                elif is_mine[i, j] and not flagged[i, j] and not is_potential[i, j]:
                    if hm_pos == (i, j):
                        print('H', end='')

                    else:
                        print('M', end='')

                elif discovered[i, j]:
                    print(mines_around[i, j], end='')

                else:
                    print('-', end='')
                if j < mines_around.cols - 1:
                    print(end=' ' * col_digits)

            print()

        tq = input('[T]ry Again - [Q]uit? ').lower()

        if tq == 't':
            minesweeper()

        elif tq == 'q':
            exit()

    elif has_won:
        t = 'turn' if turns == 1 else 'turns'
        print(f'Congrats on completing this puzzle! It took you {turns} {t} to complete.')

    input()


try:
    minesweeper()

except Exception as e:  # NOQA
    raise e
