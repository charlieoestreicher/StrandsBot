class Tile:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        return False
