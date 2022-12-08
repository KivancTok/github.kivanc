import math

import arr2D
import random

hit_mine = False
board_width = int(input('Columns: '))
col_digits = math.floor(math.log10(board_width)) + 1
board_height = int(input('Rows: '))
row_digits = math.floor(math.log10(board_height)) + 1
mines_to_place = int(input(f'Mines to place (max. {(board_width - 1) * (board_height - 1)}): '))
mines_to_place = mines_to_place if mines_to_place <= (board_width - 1) * (board_height - 1) else (board_width - 1) * (board_height - 1)
mines_to_place = mines_to_place if 0 < mines_to_place else 1
mines_left = mines_to_place

board = arr2D.Array2D.zero(board_height, board_width, 'Notminesweeper Board')
is_mine = arr2D.Array2D.false(board_height, board_width, 'Mine cells')
flagged = arr2D.Array2D.false(board_height, board_width, 'Flagged cells')
discovered = arr2D.Array2D.false(board_height, board_width, 'Discovered cells')
mines_around = arr2D.Array2D.zero(board_height, board_width, 'Mines around a cell')

while mines_to_place > 0:
    board_row = random.randint(0, board_height - 1)
    board_col = random.randint(0, board_width - 1)
    if not is_mine[board_row, board_col]:
        is_mine[board_row, board_col] = True
        mines_to_place -= 1


for i in range(board_height):
    for j in range(board_width):
        neighbors = is_mine.get_neighbors(i, j)

        mine_neighbors = 0
        for k in range(neighbors.rows):
            for m in range(neighbors.cols):
                mine_neighbors += int(neighbors[k, m])

        mine_neighbors -= board[i, j]

        mines_around[i, j] = 9 if is_mine[i, j] else (neighbors.rows * neighbors.cols - 1) - mine_neighbors


print('Hi! this is Notminesweeper. Here, you don\'t see how many mines there are, but how many mines there aren\'t. '
      'Have fun!')

while not hit_mine:
    print(f'Mines left: {mines_left}')

    print(end=' ' * row_digits)
    for i in range(mines_around.cols):
        print(end=' ')
        print(end=f'{i + 1:<{col_digits}}')

    print()

    for i in range(mines_around.rows):
        print(f'{i + 1:>{row_digits}}', end=' ')
        for j in range(mines_around.cols):
            if discovered[i, j]:
                if is_mine[i, j]:
                    print('M', end='')

                else:
                    print(mines_around[i, j], end='')

            elif flagged[i, j]:
                print('F', end='')

            else:
                print('-', end='')
            if j < mines_around.cols - 1:
                print(end=' ' * col_digits)

        print()

    fd = input('[F]lag or [D]iscover? ')

    if fd.lower() == 'd':
        dp = input('Row, column to discover (leave 1 space between row and column): ')
        dp = dp.split()
        row = int(dp[0]) - 1
        col = int(dp[1]) - 1
        discovered[row, col] = True
        if is_mine[row, col]:
            hit_mine = True

    elif fd.lower() == 'f':
        fp = input('Row, column to flag (leave a space between row and column): ')
        fp = fp.split()
        flagged[int(fp[0]) - 1, int(fp[1]) - 1] = not flagged[int(fp[0]) - 1, int(fp[1]) - 1]

        if flagged[int(fp[0]) - 1, int(fp[1]) - 1]:
            mines_left -= 1

        else:
            mines_left += 1

print('You hit a mine! :(')
input()
