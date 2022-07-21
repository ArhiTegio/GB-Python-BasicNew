class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = {
            "0":lambda x, y: x == 0 and y == 0,
            "1":lambda x, y: x > 0 and y > 0,
            "2":lambda x, y: x < 0 and y > 0,
            "3":lambda x, y: x < 0 and y < 0,
            "4":lambda x, y: x > 0 and y < 0,
        }

    def PointPosition(self):
        val = [k for k, v in self.positions.items() if v(self.x, self.y)][0]
        return "Ни к какой не принадлежит четверти" if val == "0" else val

dic_position = {
    "1":"x=1,2,3,...,∞\ny=1,2,3,...,∞",
    "2":"x=-1,-2,-3,...,-∞\ny=1,2,3,...,∞",
    "3":"x=-1,-2,-3,...,-∞\ny=-1,-2,-3,...,-∞",
    "4":"x=1,2,3,...,∞\ny=-1,-2,-3,...,-∞",
}

def Position(position: int):
        if position < 1:
            position = 1
        if position > 4:
            position = 4
        return dic_position[str(position)]


def Distence(p1:Point, p2:Point):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5