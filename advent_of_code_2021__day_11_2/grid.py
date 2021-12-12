class Grid:
    def __init__(self, grid: [[int]]):
        self.grid = grid
        self.flashes = 0
        self.ticks = 0
        self.height = len(grid)
        self.width = len(grid[0])

        self.flashed_cells: [str] = []
        self.last_flashed_cells_count = 0

    def tick(self):
        self.ticks += 1

        i = 0

        for row in self.grid:
            j = 0
            for col in row:
                self.grid[i][j] += 1
                j += 1
            i += 1

        should_refresh_grid = True

        while should_refresh_grid:
            should_refresh_grid = False

            i = 0

            for row in self.grid:
                j = 0
                for col in row:
                    if self.grid[i][j] > 9 and not self.is_flashed(j, i):
                        self.flash(j, i)

                        should_refresh_grid = True
                    j += 1
                i += 1

        for flashed_cell in self.flashed_cells:
            x = int(flashed_cell.split(';')[0])
            y = int(flashed_cell.split(';')[1])

            self.grid[y][x] = 0

        self.last_flashed_cells_count = len(self.flashed_cells)
        self.flashed_cells.clear()

    def flash(self, x: int, y: int):
        self.flashes += 1
        self.mark_flashed_cell(x, y)

        for _y in range(-1, 2):
            for _x in range(-1, 2):
                # if not middle
                if (abs(_x) + abs(_y)) != 0:
                    observing_point_x = x + _x
                    observing_point_y = y + _y

                    if observing_point_x >= 0 and observing_point_y >= 0 and observing_point_x < self.width and observing_point_y < self.height:
                        self.grid[observing_point_y][observing_point_x] += 1

    def is_flashed(self, x: int, y :int):
        if ';'.join([str(x), str(y)]) in self.flashed_cells:
            return True

        return False

    def mark_flashed_cell(self, x: int, y: int):
        if not self.is_flashed(x, y):
            self.flashed_cells.append(';'.join([str(x), str(y)]))

    @staticmethod
    def create_from_lines(lines: [str]):
        grid = []

        for line in lines:
            grid.append([int(number) for number in list(line.strip())])

        return Grid(grid)
