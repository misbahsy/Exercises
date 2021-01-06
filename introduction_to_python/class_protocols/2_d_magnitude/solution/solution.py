import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x =x
        self.y = y
        self.z = z
    
    def mag(self):
        return(math.sqrt(self.x**2 + self.y**2 + self.z**2))

    def __str__(self):
        return(f'(x = {self.x}, y = {self.y}, z = {self.z})')
    
    def __add__(self, other):
        return(Vector3D(self.x + other.x, self.y + other.y, self.z + other.z))
    
    def __lt__(self, other):
        return( self.mag() < other.mag())
    
    def __gt__(self, other):
        return( self.mag() > other.mag())

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __eq__(self, other):
        return( self.x == other.x and self.y == other.y and self.z == other.z)

    def __abs__(self):
        return(self.mag())