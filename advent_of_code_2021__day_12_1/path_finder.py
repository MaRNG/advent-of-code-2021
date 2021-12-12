class PathFinder:
    START = 'start'
    END = 'end'

    def __init__(self, map_data: [str]):
        self.map_data = {}
        self.prepare_graph(map_data)

        self.routes = []

    def prepare_graph(self, map_data: [str]) -> {str: str}:
        map_data_item: str
        for map_data_item in map_data:
            (start, end) = map_data_item.strip().split('-', 2)

            if start not in self.map_data:
                self.map_data[start] = []

            if end not in self.map_data:
                self.map_data[end] = []

            self.map_data[start] += [end]
            self.map_data[end] += [start]

    def find_all_possible_paths(self):
        self.routes = []

        self.find_path(PathFinder.START, [PathFinder.START])

        routes = len(self.routes)
        self.routes = []

        return routes

    def find_path(self, current: str, path: [str]):
        if current == PathFinder.END:
            self.routes.append(path)
            return

        target_vertex: str

        for target_vertex in self.map_data[current]:
            if target_vertex != PathFinder.START and (not target_vertex.islower() or target_vertex not in path):
                self.find_path(target_vertex, path + [target_vertex])



