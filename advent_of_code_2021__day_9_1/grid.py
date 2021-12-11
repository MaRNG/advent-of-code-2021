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

    def get_risk_level(self) -> int:
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
                    lowest_points.append(int(col))

                x += 1

            y += 1

        return sum(lowest_points) + (1 * len(lowest_points))
