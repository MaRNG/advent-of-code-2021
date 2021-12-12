import typing


class VentsMap:
    def __init__(self):
        self.map = {}

    def add_vent_coordinates(self, start: typing.Tuple[int, int], end: typing.Tuple[int, int]):

        # vertical vent
        if start[0] == end[0]:
            x = start[0]
            y = []

            # inclusive end
            for i in range(min(start[1], end[1]), (max(start[1], end[1]) + 1)):
                y.append(i)

            for i_y in y:
                formatted_coordinates = '{x_axis},{y_axis}'.format(x_axis=x, y_axis=i_y)

                if formatted_coordinates in self.map:
                    self.map[formatted_coordinates] += 1
                else:
                    self.map[formatted_coordinates] = 1

        # horizontal vent
        elif start[1] == end[1]:
            x = []
            y = start[1]

            # inclusive end
            for i in range(min(start[0], end[0]), (max(start[0], end[0]) + 1)):
                x.append(i)

            for i_x in x:
                formatted_coordinates = '{x_axis},{y_axis}'.format(x_axis=i_x, y_axis=y)

                if formatted_coordinates in self.map:
                    self.map[formatted_coordinates] = self.map[formatted_coordinates] + 1
                else:
                    self.map[formatted_coordinates] = 1

    def get_overlapped_vents_count(self) -> int:
        output = 0

        for (coordinates_index, coordinates) in self.map.items():
            if coordinates > 1:
                output += 1

        return output
