import math

print "hello"

class Line:
    
	def __init__(self,coor1,coor2):
	    	self.coor1 = coor1
		self.coor2 = coor2
	def distance(self):
    		x = self.coor1.x - self.coor2.x
		y = self.coor1.y - self.coor2.y
		t = math.sqrt(x*x + y*y)
		return t:w 
	def slope(self):
		px = self.coor2.x - self.coor1.x
		py = self.coor2.y - self.coor1.y
		return px/py
	def __str__(self):
		return "(%s,%s)->(%s,%s)", self.coor1.x, self.coor1.y, self.coor2.x, self.coor2.y

l = Line()
print 'Distance ', l.distance()
print 'Slope: ', l.slope() 
