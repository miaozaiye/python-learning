class Student(object):

	@property
	def birth(self):
		return self._birth
	

	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self.birth
	


s = Student()
s.birth = 1981
print s.age



class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		self._height = value

	@property
	def resolution(self):
	    self._resolution = self._width * self._height
	    return self._resolution

s = Screen()
s.width = 1024
s.height = 768
print (s.resolution)










