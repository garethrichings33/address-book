class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        print("hello")
        self._x = value


coord = Coordinate(1, 2)
coord.x = 3
print(coord.x)
