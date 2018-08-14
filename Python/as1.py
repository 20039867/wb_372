class Cylinder(object):
	pi = 3.14
	
	def __init__(self,height=1,radius=1):
		self.height = 1
		self.radius = 1
	
	def volume(self):
		j = Cylinder.pi*self.radius*self.radius*self.height
		return j
	
	def surface_area(self):
		j = 2*Cylinder.pi*self.radius*self.radius + 2*Cylinder.pi*self.radius*self.height
		return j

/* /* /* /* /* /* /* /*  */ */ */ */ */ */ */ */

import math
class Line:
    
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
    	x = self.coor1.x - self.coor2.x
		y = self.coor1.y - self.coor2.y
		t = math.sqrt(x*x + y*y)
		return t

	def slope(self):
		px = self.coor2.x - self.coor1.x
		py = self.coor2.y - self.coor1.y
		return px/py

	
	def __str__(self):
		return '(' + self.coor1.x + ',' + self.coor1.y + ')' + "->" +  '(' +
		self.coor2.x + ',' + self.coor2.y + ')'

