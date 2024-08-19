from searching_framework import Problem, astar_search


class Maze(Problem):

    def __init__(self, initial, walls, size, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.size = size

    def valid(self, state):
        return state not in self.walls and (0 <= state[0] < self.size and 0 <= state[1] < self.size)

    def move_u_d_l(self, state, direction, increment):
        state = list(state)
        state[direction] += increment
        state = tuple(state)
        if not self.valid(state):
            return None
        return state

    def move_r(self, state, increment):
        state = list(state)
        for i in range(increment):
            state[0] += 1
            if not self.valid(tuple(state)):
                return None

        return tuple(state)

    def successor(self, state):
        neighbors = {}
        r2 = self.move_r(state, 2)
        if r2 is not None:
            neighbors["Desno 2"] = r2
        r3 = self.move_r(state, 3)
        if r3 is not None:
            neighbors["Desno 3"] = r3
        l1 = self.move_u_d_l(state, 0, -1)
        if l1 is not None:
            neighbors["Levo"] = l1
        d = self.move_u_d_l(state, 1, -1)
        if d is not None:
            neighbors["Dolu"] = d
        u = self.move_u_d_l(state, 1, 1)
        if u is not None:
            neighbors["Gore"] = u

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return super().goal_test(state)

    def h(self, node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])) / 3


if __name__ == '__main__':
    n = int(input())
    walls = []
    for i in range(int(input())):
        x, y = map(int, input().split(","))
        walls.append((x, y))
    man = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    maze = Maze(man, walls, n, house)

    problem = astar_search(maze)

    if problem is not None:
        print(problem.solution())
