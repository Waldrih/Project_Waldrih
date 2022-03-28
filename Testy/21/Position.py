from pygame import Surface

class Position:
    def __init__(self, x: int, y: int, image: Surface, N: bool, E: bool, S: bool, W: bool):
        self.x = x
        self.y = y
        self.image = image
        self.N = N
        self.E = E
        self.S = S
        self.W = W
