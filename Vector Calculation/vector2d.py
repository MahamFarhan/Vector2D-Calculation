import math
class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self._x = x 
        self._y = y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value
    
    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)
    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x - other._x, self._y - other._y)
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self._x * scalar, self._y * scalar)
    
    def dot (self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._x * other._x + self._y * other._y
    def magnitude(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
    def __str__(self):
        return f"Vector2D({self._x}, {self._y})"
    def __repr__(self):
        return f"Vector2D({self._x!r}, {self._y!r})"