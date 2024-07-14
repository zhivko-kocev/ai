from searching_framework import Problem, breadth_first_graph_search


class Football(Problem):
    def __init__(self, initial, goal, players, invalid_ball_positions):
        super().__init__(initial, goal)
        self.players = players
        self.invalid_ball_positions = invalid_ball_positions

    def check_valid(self, state):
        player, ball, has_kicked = state

        return ball not in self.invalid_ball_positions and (0 <= ball[0] <= 7 and 0 <= ball[1] <= 5) \
            and (0 <= player[0] <= 7 and 0 <= player[1] <= 5) and ball not in self.players and player not in self.players

    def move(self, state, direction):
        player, ball, has_kicked = state
        player = list(player)
        ball = list(ball)
        if direction == "R":
            player, ball, has_kicked = self.right(player, ball)
        if direction == "U":
            player, ball, has_kicked = self.up(player, ball)
        if direction == "D":
            player, ball, has_kicked = self.down(player, ball)
        if direction == "UR":
            player, ball, has_kicked = self.up_right(player, ball)
        if direction == "DR":
            player, ball, has_kicked = self.down_right(player, ball)

        new_state = (tuple(player), tuple(ball), has_kicked)
        if self.check_valid(new_state):
            return new_state
        else:
            return None

    def right(self, player, ball):
        player[0] += 1
        if player == ball:
            ball[0] += 1
            return player, ball, True
        return player, ball, False

    def up(self, player, ball):
        player[1] += 1
        if player == ball:
            ball[1] += 1
            return player, ball, True
        return player, ball, False

    def down(self, player, ball):
        player[1] -= 1
        if player == ball:
            ball[1] -= 1
            return player, ball, True
        return player, ball, False

    def up_right(self, player, ball):
        player[0] += 1
        player[1] += 1
        if player == ball:
            ball[0] += 1
            ball[1] += 1
            return player, ball, True
        return player, ball, False

    def down_right(self, player, ball):
        player[1] -= 1
        player[0] += 1
        if player == ball:
            ball[0] += 1
            ball[1] -= 1
            return player, ball, True
        return player, ball, False

    def successor(self, state):
        neighbours = dict()
        # Gore
        up = self.move(state, "U")
        if up is not None:
            if up[2]:
                neighbours["Turni topka gore"] = up
            else:
                neighbours["Pomesti coveche gore"] = up
        # Dolu
        down = self.move(state, "D")
        if down is not None:
            if down[2]:
                neighbours["Turni topka dolu"] = down
            else:
                neighbours["Pomesti coveche dolu"] = down
        # Desno
        right = self.move(state, "R")
        if right is not None:
            if right[2]:
                neighbours["Turni topka desno"] = right
            else:
                neighbours["Pomesti coveche desno"] = right
        # Gore-Desno
        ur = self.move(state, "UR")
        if ur is not None:
            if ur[2]:
                neighbours["Turni topka gore-desno"] = ur
            else:
                neighbours["Pomesti coveche gore-desno"] = ur
        # Dolu-Desno
        dr = self.move(state, "DR")
        if dr is not None:
            if dr[2]:
                neighbours["Turni topka dolu-desno"] = dr
            else:
                neighbours["Pomesti coveche dolu-desno"] = dr

        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal


if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))
    football = Football((player, ball, False),
                        ((7, 2), (7, 3)),
                        ((3, 3), (5, 4)),
                        ((2, 4), (3, 4), (4, 4), (2, 3), (3, 3), (4, 3), (2, 2), (3, 2), (4, 2),
                         (4, 5), (5, 5), (6, 5), (4, 4), (5, 4), (6, 4), (4, 3), (5, 3), (6, 3)))
    sol = breadth_first_graph_search(football)
    if sol is not None:
        print(sol.solution())
