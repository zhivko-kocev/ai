from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, snake: tuple, red_apples: tuple):
        super().__init__(snake)
        self.red_apples = red_apples

    def right(self, head, direction):
        if direction == 'S':
            head[0] -= 1
            direction = 'W'
        elif direction == 'N':
            head[0] += 1
            direction = 'E'
        elif direction == 'W':
            head[1] += 1
            direction = 'N'
        elif direction == 'E':
            head[1] -= 1
            direction = 'S'
        return head, direction

    def left(self, head, direction):
        if direction == 'S':
            head[0] += 1
            direction = 'E'
        elif direction == 'N':
            head[0] -= 1
            direction = 'W'
        elif direction == 'W':
            head[1] -= 1
            direction = 'S'
        elif direction == 'E':
            head[1] += 1
            direction = 'N'
        return head, direction

    def straight(self, head, direction):
        if direction == 'S':
            head[1] -= 1
        elif direction == 'N':
            head[1] += 1
        elif direction == 'W':
            head[0] -= 1
        elif direction == 'E':
            head[0] += 1
        return head, direction

    def move(self, state, dir):
        body, direction, green_apples = state
        head = list(body[0])
        tmp1 = head.copy()
        body = list(body)
        if dir == 'R':
            head, direction = self.right(head, direction)
        if dir == 'L':
            head, direction = self.left(head, direction)
        if dir == 'S':
            head, direction = self.straight(head, direction)
        body[0] = tuple(head)
        for i in range(1, len(body)):
            tmp2 = body[i]
            body[i] = tuple(tmp1)
            tmp1 = tmp2
        tail = body[1:]
        if ((body[0][0] < 0 or body[0][0] > 9) or (body[0][1] > 9 or body[0][1] < 0)) \
                or body[0] in self.red_apples or body[0] in tail:
            return None
        if body[0] in state[2]:
            green_apples = list(state[2])
            green_apples.remove(body[0])
            body.append((body[-1][0], body[-1][1] + 1))
        return tuple(body), direction, tuple(green_apples)

    def successor(self, state):
        neighbours = dict()

        # Pravo
        straight = self.move(state, 'S')
        if straight is not None:
            neighbours["ProdolzhiPravo"] = straight

        # Desno
        right = self.move(state, 'R')
        if right is not None:
            neighbours["SvrtiDesno"] = right

        # Levo
        left = self.move(state, 'L')
        if left is not None:
            neighbours["SvrtiLevo"] = left



        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == "__main__":
    broj_zeleni = int(input())
    zeleni = list()
    for i in range(broj_zeleni):
        zeleni.append(tuple(map(int, input().split(','))))

    broj_crveni = int(input())
    crveni = list()
    for i in range(broj_crveni):
        crveni.append(tuple(map(int, input().split(','))))

    snake = Snake((((0, 7), (0, 8), (0, 9)), 'S', tuple(zeleni)), tuple(crveni))

    sol = breadth_first_graph_search(snake)
    if sol is not None:
        print(sol.solution())
