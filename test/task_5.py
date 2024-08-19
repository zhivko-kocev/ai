class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position : {self.x}, {self.y}"

    def move(self):
        pass


class LeftAgent(Agent):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


if __name__ == "__main__":
    agent = LeftAgent()
    print(agent)
