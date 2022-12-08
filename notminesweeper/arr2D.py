class Array2D:
    boards = []

    def __init__(self, rows, cols, data: list = None, name: str = None):
        if data is None:
            data = [[None for _ in range(cols)] for _ in range(rows)]
        if name is None:
            name = 'array2D_instance'
        self.name = name
        self.rows = rows
        self.cols = cols
        self.table = [[data[x][y] for y in range(cols)] for x in range(rows)]
        self.boards.append(self)

    def __getitem__(self, index):
        if isinstance(index[0], slice) and isinstance(index[1], slice):
            i0st = index[0].start if index[0].start is not None else 0
            i0so = index[0].stop if index[0].stop is not None else 0
            i0sp = index[0].step if index[0].step is not None else 1
            i1st = index[1].start if index[1].start is not None else 0
            i1so = index[1].stop if index[1].stop is not None else 0
            i1sp = index[1].step if index[1].step is not None else 1

            arr = self.zero((i0so - i0st) // i0sp, (i1so - i1st) //
                            i1sp)

            sl0 = slice(index[0].start, index[0].stop, index[0].step)
            sl1 = slice(index[1].start, index[1].stop, index[1].step)

            for i, v in enumerate(self.table[sl0]):
                for j, w in enumerate(v[sl1]):
                    arr[i, j] = w

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
                string += '%s ' % str(col)
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

    def get_neighbors(self, *idx):
        row = idx[0]
        col = idx[1]
        if row == 0:
            if col == 0:
                return self[:2, :2]

            elif col % self.cols == self.cols - 1:
                return self[:2, -2:]

            else:
                return self[:2, col - 1:col + 2]

        elif row % self.rows == self.rows - 1:
            if col == 0:
                return self[-2:, :2]

            elif col % self.cols == self.cols - 1:
                return self[-2:, -2:]

            else:
                return self[-2:, col - 1:col + 2]

        else:
            if col == 0:
                return self[row - 1:row + 2, :2]

            elif col % self.cols == self.cols - 1:
                return self[row - 1:row + 2, -2:]

            else:
                return self[row - 1:row + 2, col - 1:col + 2]

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

    def get_board(self, name):
        for i, v in enumerate(self.boards):
            if v.name == name:
                return self.boards[i]
        return 'Board not found :/'
