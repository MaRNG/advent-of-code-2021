class Grid:
    def __init__(self, data: [[int]]):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    @staticmethod
    def parse_raw_data(rows: [str]):
        parsed_data = []

        for row in rows:
            parsed_data.append(list(row.strip()))

        return Grid(parsed_data)

    def find_lowest_points(self) -> [str]:
        lowest_points = []

        y = 0
        for row in self.data:
            x = 0

            for col in row:
                has_lower_point = False

                # left
                if x > 0 and row[x-1] <= col:
                    has_lower_point = True
                # right
                if x < (self.width - 1) and row[x+1] <= col:
                    has_lower_point = True
                # top
                if y > 0 and self.data[y-1][x] <= col:
                    has_lower_point = True
                # bottom
                if y < (self.height - 1) and self.data[y+1][x] <= col:
                    has_lower_point = True

                if not has_lower_point:
                    lowest_points.append(';'.join([str(x), str(y)]))

                x += 1

            y += 1

        return lowest_points

    def find_three_largest_basins(self) -> int:
        output = 1
        basins = []
        lowest_points = self.find_lowest_points()

        for lowest_point in lowest_points:
            basin = []

            opened_cells = [lowest_point]
            closed_cells = []

            while len(opened_cells) > 0:
                for opened_cell in opened_cells:
                    x = int(opened_cell.split(';', 2)[0])
                    y = int(opened_cell.split(';', 2)[1])

                    opened_cells.remove(opened_cell)
                    closed_cells.append(opened_cell)
                    basin.append(self.data[y][x])

                    for cell_to_open in self._get_cells_to_open(x, y):
                        if cell_to_open not in opened_cells and cell_to_open not in closed_cells:
                            opened_cells.append(cell_to_open)

            basins.append(basin)

        calculated_basins = []

        for basin in basins:
            calculated_basins.append(len(basin))

        calculated_basins.sort()

        for largest_basin in calculated_basins[-3:]:
            output = output * largest_basin

        return output

    def _get_cells_to_open(self, x: int, y: int) -> [str]:
        opened_cells = []

        if x > 0 and int(self.data[y][x - 1]) != 9:
            opened_cells.append(';'.join([str(x - 1), str(y)]))

        if x < (self.width - 1) and int(self.data[y][x + 1]) != 9:
            opened_cells.append(';'.join([str(x + 1), str(y)]))

        if y > 0 and int(self.data[y - 1][x]) != 9:
            opened_cells.append(';'.join([str(x), str(y - 1)]))

        if y < (self.height - 1) and int(self.data[y + 1][x]) != 9:
            opened_cells.append(';'.join([str(x), str(y + 1)]))

        return opened_cells
