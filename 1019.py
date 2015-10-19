class Animal(object):
	pass

# class 1
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

# kinds of animals
class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

class Runnable(object):
	def run(self):
		print ('Running...')

class Flyable(object):
	def fly(self):
		print ('Flying...')


class Bat(Mammal,Flyable):
	pass

class Dog(Mammal,Runnable):
	pass
	