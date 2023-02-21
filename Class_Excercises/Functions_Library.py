from math import cos, hypot, sin, pi, atan2

eps = 1e-4

class Point:
    def __init__(self, *args):
        self.coords = list(args)
        self.x = args[0]
        self.y = args[1]
        self.angle = atan2(-self.y, -self.x)

    def __eq__(self, other):
        def comp(a, b):
            return abs(a-b) < eps

        if len(self.coords) != len (other.coords):
            return "Arithmetic Error"
        else:
            for i, coord in enumerate(self.coords):
                if comp(coord, other.coords[i]) == False:
                    return False
        return True

    def rotate(self, theta):
        theta = theta * pi / 180
        x = self.x
        y = self.y
        self.x = x * cos(theta) - y * sin(theta)
        self.y = x * sin(theta) + y * cos(theta)

    def distance(self, p2):
        dx = self.x - p2.coords[0]
        dy = self.y - p2.coords[1]
        return hypot(dx, dy)

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"