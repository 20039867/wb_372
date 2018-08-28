import math


#Problem 1

class Line (object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance (self):
        xsum = self.coor1[0] - self.coor2[0]
        ysum = self.coor1[1] - self.coor2[1]
        sum = xsum*xsum + ysum*ysum
        sum = math.sqrt(sum)
        return sum

    def slope (self):
        xsum = self.coor1[0] - self.coor2[0]
        ysum = self.coor1[1] - self.coor2[1]
        slope = float(ysum)/float(xsum)
        return slope

coordinate1 = (3,2)
coordiante2 = (8,10)

li = Line(coordinate1, coordiante2)

print "Distance: ", li.distance()

print "Slope: " , li.slope()

#Problem 2
class Cylinder(object):

        def __init__(self, height, radius):
            self.height = height
            self.radius = radius

        def volume (self):
            volume = math.pi * self.radius * self.radius * self.height
            return volume

        def surface_area(self):
            sa = 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * self.radius
            return sa


c = Cylinder(2,3)
print "volume: ", c.volume()
print "Surface area: ", c.surface_area()
