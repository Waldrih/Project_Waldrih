from pygame import Surface
from Board import Board

class Position:
    def __init__(self, x: int, y: int, board: Board ):
        self.x = x
        self.y = y
        self.board = Board

    def __str__(self):
        return f"Pozycja x: {self.x}. y: {self.y}"

