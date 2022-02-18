#1)
class String:
    def _init_(self, chars):
        self.chars = chars

    def getString(self):
        return self.chars

    def uppercase(self):
        return self.chars.upper()

#S1 = String("Ersultan")
#S2 = String("Beibarys")
#print(S1.getString(), S2.getString(), end = '')
#print(sep = "\n")
#print(S1.uppercase(), S2.uppercase(), end = '')

#2)
class Shape:
    def _init_(self, area):
        self.area = 0

class Rectangle(Shape):
    def _init_(self, length, width, area):
        self.length = length
        self.width = width
        super()._init_(area)

    def get_area(self):
        return self.length * self.width

#S1 = Rectangle(5, 2, 0)
#S2 = Rectangle(4, 3, 0)
#print (S1.get_area(), S2.get_area(), sep = '\n')

#4)
class Point:
    def _init_(self, a,b):
        self.a = a
        self.b = b
    def show(self):
        print(self.a, self.b)

    def move(self, x, y):
        self.a, self.b = x, y

    def dist(self, d):
        return ((self.a - d.a)*2 + (self.b - d.b)*2)
    
#l = Point(1, 2)
#m = Point(4, 5)
#print(l.dist(m))

#4)
