from math import sqrt
from unit_tester import test


def testsuite():
    # r = Rectangle(Point(0, 0), 15, 5)
    # test(r.area_of_rectangle() == 75)
    # test(r.perimeter_of_rectangle() == 40)
    # r = Rectangle(Point(100, 50), 10, 5)
    # test(r.width == 10 and r.height == 5)
    # r.flip()
    # test(r.width == 5 and r.height == 10)
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))
    # l = Rectangle((0, 0), 10, 10)
    # test(l.hit_boxes(Point(10, 10), 10, 10))

class Point:
    """point class represents and manupulates x,y coords"""
    def __init__(self, x=0, y=0):
        """create a new point at x, y"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """compute my distance from origin"""
        return ((self.x ** 2)+(self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """return the midpoint of points p1 and p2"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance(self, target):
        return sqrt((target.x - self.x) ** 2 + (target.y - self.y) ** 2)

    def reflect_x(self):
        return -self.y

    def slope_from_origin(self,):
        """ask for help"""
        return self.y - self.x

    def get_line_to(self, pt):
        slope = (self.y - pt.y) / (self.x - pt.x)
        return slope, self.y - self.x * slope


class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2}".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area_of_rectangle(self):
        return self.width * self.height

    def perimeter_of_rectangle(self):
        return self.width * 2 + self.height * 2

    def flip(self):
        (self.width, self.height) = (self.height, self.width)
        return self.width, self.height

    def contains(self, point_coords):
        if point_coords.x < self.width and point_coords.x >= 0:
            if point_coords.y < self.height and point_coords.y >= 0:
                return True
        else:
            return False

    def hit_boxes(self, point_cords, height, width):
        y = point_cords.y + height
        x = point_cords.x + width
        in_square = False
        for i in range(point_cords.y, height, height - 1):
            in_square = self.contains(Point(point_cords.y, i))
        if in_square:
            return True
        for i in range(x, width, width - 1):
            in_square = self.contains(Point(i, height))
        if in_square:
            return True
        for i in range(y, height, -height - 1):
            in_square = self.contains(Point(width, i))
        if in_square:
            return True
        for i in range(x, width, -width - 1):
            in_square = self.contains(Point(i, height))
        if in_square:
            return True
        in_square = self.contains(Point(width, height))
        if in_square:
            return True
        in_square = self.contains(Point(point_cords.x, height))
        if in_square:
            return True
        in_square = self.contains(Point(width, point_cords.y))
        if in_square:
            return True
        in_square = self.contains(Point(point_cords.x, point_cords.y))
        if in_square:
            return True
        return False


def same_coordinates(c1, c2):
    return (c1.x == c2.x) and (c1.y == c2.y)


# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)
# print("box: ", box)
# print("bomb: ", bomb)

# r = Rectangle(Point(10, 5), 100, 50)
# print(r)
# r.grow(25, -10)
# print(r)
# r.move(-10, 10)
# print(r)

# p1 = Point(3, 4)
# p2 = copy.copy(p1)
# print(p1 is p2)
# print(same_coordinates(p1, p2))
# box2 = copy.deepcopy(box)
# print(box2 is box)


testsuite()
