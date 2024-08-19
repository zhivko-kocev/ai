from searching_framework import Problem, astar_search


class Maze(Problem):

    def __init__(self, initial, green_circles, goal=None):
        super().__init__(initial, goal)
        self.green_circles = green_circles

    def valid_state(self, man, house):
        return (man in self.green_circles or man == house[0]) and ((0 <= man[0] <= 4) and (0 <= man[1] <= 8))

    def move_man_diagonal(self, man, increment):
        man = list(man)
        man[1] += abs(increment)
        man[0] += increment
        man = tuple(man)
        return man

    def move_man_up(self, man, increment):
        man = list(man)
        man[1] += increment
        man = tuple(man)

        return man

    def move(self, man, house, dire):

        house = self.move_house(house)

        if dire == "S":
            man = self.move_man_up(man, 0)
        if dire == "U1":
            man = self.move_man_up(man, 1)
        if dire == "U2":
            man = self.move_man_up(man, 2)
        if dire == "UR1":
            man = self.move_man_diagonal(man, 1)
        if dire == "UR2":
            man = self.move_man_diagonal(man, 2)
        if dire == "LR1":
            man = self.move_man_diagonal(man, -1)
        if dire == "LR2":
            man = self.move_man_diagonal(man, -2)

        if not self.valid_state(man, house):
            return None

        return man, house

    def move_house(self, house):
        coordinates, direction = house
        coordinates = list(coordinates)
        coordinates[0] += direction
        coordinates = tuple(coordinates)
        if direction == -1 and coordinates[0] == 0:
            direction = 1

        if direction == 1 and coordinates[0] == 4:
            direction = -1

        return coordinates, direction

    def successor(self, state):
        neighbors = {}
        man, house = state

        stop = self.move(man, house, "S")
        if stop is not None:
            neighbors["Stoj"] = stop

        up_1 = self.move(man, house, "U1")
        if up_1 is not None:
            neighbors["Gore 1"] = up_1

        up_2 = self.move(man, house, "U2")
        if up_2 is not None:
            neighbors["Gore 2"] = up_2

        ur_1 = self.move(man, house, "UR1")
        if ur_1 is not None:
            neighbors["Gore-desno 1"] = ur_1

        ur_2 = self.move(man, house, "UR2")
        if ur_2 is not None:
            neighbors["Gore-desno 2"] = ur_2

        ul_1 = self.move(man, house, "LR1")
        if ul_1 is not None:
            neighbors["Gore-levo 1"] = ul_1

        ul_2 = self.move(man, house, "LR2")
        if ul_2 is not None:
            neighbors["Gore-levo 2"] = ul_2

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        goal = state[1]
        goal = goal[0]
        return state[0] == goal

    def h(self, node):
        state = node.state[0]
        goal = node.state[1]
        goal = goal[0]
        return abs(goal[1] - state[1]) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    x_man, y_man = tuple(map(int, input().split(",")))

    x_house, y_house = tuple(map(int, input().split(",")))

    direction = input()

    if direction == "desno":
        direct = 1
    else:
        direct = -1

    problem = Maze(((x_man, y_man), ((x_house, y_house), direct)), allowed)

    sol = astar_search(problem)
    if sol is not None:
        print(sol.solution())
