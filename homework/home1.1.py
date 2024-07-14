from searching_framework import Problem, astar_search, depth_first_graph_search, best_first_graph_search, \
    uniform_cost_search


class Pacman(Problem):

    # ((pac1,pac2,pac3...),(palet1,palet2,palet3...))

    def __init__(self, initial, walls, height, width, pacman_pos, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.height = height
        self.width = width
        self.pacman_pos = pacman_pos

    def successor(self, state):
        neighbors = {}
        #all the possible states
        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return all([True if child == self.pacman_pos else False for child in state[0]]) and len(state[1]) == 0

    def manhattan_distance(self, child):
        return abs(child[0] - self.pacman_pos[0]) + abs(child[1] - self.pacman_pos[1])

    def h(self, node):
        sum_children = 0
        children, palettes = node.state
        for child in children:
            sum_children += self.manhattan_distance(child)
        return sum_children


if __name__ == '__main__':
    children = ((0, 2), (4, 0), (8, 2), (2, 5))
    walls = ((2, 0), (6, 0), (0, 3), (0, 5), (8, 5), (3, 3), (4, 3), (5, 3), (6, 3), (4, 4), (6, 4))
    pacman_pos = (5, 4)
    palettes = (
        (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (1, 4), (2, 4), (3, 4), (7, 4), (1, 3), (2, 3), (7, 3), (2, 2), (6, 2),
        (7, 2), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (0, 0))

    game = Pacman((children, palettes), walls, 6, 9, pacman_pos)

    result = astar_search(game)

    print(result)
