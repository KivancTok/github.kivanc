import math
from typing import Self


def _lsrepr(slc):
    start = '' if slc.start is None else str(slc.start)
    stop = '' if slc.stop is None else str(slc.stop)
    step = '' if slc.step is None else str(slc.step)
    return f'{start}:{stop}:{step}'


def _sign(num):
    if num > 0:
        return 1

    if num == 0:
        return 0

    if num < 0:
        return -1


def _closer(num):
    return num - _sign(num)


def _bound(lower, upper, num):
    return max(lower, min(upper, num))


class Array2D:
    def __init__(self, rows, cols, data: list = None, name: str = None):
        if data is None:
            data = [[None for _ in range(cols)] for _ in range(rows)]
        if name is None:
            name = 'array2D_instance'
        self.name = name
        self.rows = rows
        self.cols = cols
        self.table = [[data[x][y] for y in range(cols)] for x in range(rows)]

    def __getitem__(self, index):
        row_is_slice = isinstance(index[0], slice)
        col_is_slice = isinstance(index[1], slice)
        if row_is_slice and col_is_slice:
            i0sp = index[0].step if index[0].step is not None else 1
            i0st = index[0].start if index[0].start is not None else (0 if _sign(i0sp) > 0 else self.rows - 1)
            i0so = index[0].stop if index[0].stop is not None else (self.rows if _sign(i0sp) > 0 else -1)
            i1sp = index[1].step if index[1].step is not None else 1
            i1st = index[1].start if index[1].start is not None else (0 if _sign(i1sp) > 0 else self.cols - 1)
            i1so = index[1].stop if index[1].stop is not None else (self.cols if _sign(i1sp) > 0 else -1)

            arr = self.null(math.ceil((i0so - i0st) / i0sp), math.ceil((i1so - i1st) / i1sp), name=f'arr_slice row {_lsrepr(index[0])} col {_lsrepr(index[1])}')

            for i, ai in zip(range(i0st, i0so, i0sp), range(arr.rows)):
                v = self.table[i]
                for j, aj in zip(range(i1st, i1so, i1sp), range(arr.cols)):
                    w = v[j]
                    arr[ai, aj] = w

            return arr

        if row_is_slice and not col_is_slice:
            isp = index[0].step if index[0].step is not None else 1
            ist = index[0].start if index[0].start is not None else (0 if _sign(isp) > 0 else self.rows - 1)
            iso = index[0].stop if index[0].stop is not None else (self.rows if _sign(isp) > 0 else -1)

            arr = self.null(math.ceil((iso - ist) / isp), 1, name=f'arr_slice row {_lsrepr(index[0])} col {index[1]}')

            for i, ai in zip(range(ist, iso, isp), range(arr.rows)):
                v = self.table[i]
                arr[ai, 0] = v[index[1]]

            return arr

        if not row_is_slice and col_is_slice:
            isp = index[1].step if index[1].step is not None else 1
            ist = index[1].start if index[1].start is not None else (0 if _sign(isp) > 0 else self.cols - 1)
            iso = index[1].stop if index[1].stop is not None else (self.cols if _sign(isp) > 0 else -1)

            arr = self.null(1, math.ceil((iso - ist) / isp), name=f'arr_slice row {index[0]} col {_lsrepr(index[1])}')

            v = self.table[index[0]][index[1]]

            for i in range(arr.cols):
                arr[0, i] = v[i]

            return arr
        return self.table[index[0]][index[1]]

    def __setitem__(self, index, value):
        self.table[index[0]][index[1]] = value

    def __iter__(self):
        return iter(self.table)

    def __repr__(self):
        string = '%ix%i Array2D \'%s\': {\n' % (self.cols, self.rows, self.name)
        for row in self.table:
            string += '\t'
            for col in row:
                string += f'{str(col)} '
            string += '\n'
        string += '}'
        return string

    def nullify(self):
        self.table = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def zero_out(self):
        self.table = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def add_rows(self, rows):
        for i in range(rows):
            self.table.append([None for _ in range(self.cols)])
            self.rows += 1

    def add_cols(self, cols):
        for i in range(cols):
            for row in self.table:
                row.append(None)
            self.cols += 1

    def get_neighbors(self, row_range, col_range, *idx) -> Self:
        row = idx[0]
        col = idx[1]

        return self[_bound(0, self.rows - 1, row - row_range):_bound(0, self.rows - 1, row + row_range) + 1, _bound(0, self.cols - 1, col - col_range):_bound(0, self.cols - 1, col + col_range) + 1]

    @classmethod
    def zero(cls, rows, cols, name: str = None):
        if name is None:
            name = 'array2D_instance'
        arr = cls(rows, cols, name=name)
        arr.zero_out()
        return arr

    @classmethod
    def false(cls, rows, cols, name: str = None):
        if name is None:
            name = 'array2D_instance'
        arr = cls(rows, cols, name=name)
        arr.zero_out()
        for i in range(rows):
            for j in range(cols):
                arr[i, j] = False
        return arr

    @classmethod
    def null(cls, rows, cols, name: str = None):
        arr = cls(rows, cols, name=name)
        arr.nullify()
        return arr

    def __len__(self):
        return self.rows * self.cols
