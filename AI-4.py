class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.num_nodes = len(graph)
        self.colors = [''] * self.num_nodes
        self.available_colors = colors
        self.min_colors = self.num_nodes
        self.best_colors = []

    def is_safe(self, vertex, color):
        for i in range(self.num_nodes):
            if self.graph[vertex][i] == 1 and self.colors[i] == color:
                return False
        return True

    def backtracking(self, vertex):
        if vertex == self.num_nodes:
            if len(set(self.colors)) < self.min_colors:
                self.min_colors = len(set(self.colors))
                self.best_colors = self.colors.copy()
            return

        for color in self.available_colors:
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                self.backtracking(vertex + 1)
                self.colors[vertex] = ''

    def branch_and_bound(self, vertex):
        if vertex == self.num_nodes:
            num_colors = len(set(self.colors))
            if num_colors < self.min_colors:
                self.min_colors = num_colors
                self.best_colors = self.colors.copy()
            return

        for color in self.available_colors:
            if self.is_safe(vertex, color):
                original_color = self.colors[vertex]
                self.colors[vertex] = color

                min_colors_estimate = self.estimate_min_colors(vertex + 1)
                if min_colors_estimate < self.min_colors:
                    self.branch_and_bound(vertex + 1)

                self.colors[vertex] = original_color

    def estimate_min_colors(self, vertex):
        for i in range(vertex, self.num_nodes):
            self.colors[i] = ''

        for i in range(self.num_nodes - 1, -1, -1):
            if self.colors[i] == '':
                available_colors = set(self.available_colors)
                for j in range(self.num_nodes):
                    if self.graph[i][j] == 1 and self.colors[j] != '':
                        available_colors.discard(self.colors[j])
                if available_colors:
                    self.colors[i] = available_colors.pop()

        return len(set(self.colors))

    def solve(self):
        self.backtracking(0)
        self.colors = [''] * self.num_nodes
        self.branch_and_bound(0)

        return self.min_colors, self.best_colors

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    colors = ['Red', 'Green', 'Blue']  

    coloring_problem = GraphColoring(graph, colors)
    min_colors, best_colors = coloring_problem.solve()

    print("Minimum number of colors:", min_colors)
    print("Coloring:", best_colors)
