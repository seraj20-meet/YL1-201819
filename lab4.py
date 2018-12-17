rec1= Rectangle(3,4)
print(rec1.Area())
print(rec1.perimeter())

class person(object):
	def __init__(self, name, age, city, gender):
		self.name= name
		self.age = age
		self.city = city
		self.gender = gender
def eat(self, food):
	print(self.name + " has eaten" + food)
def sleep(self,hours):
	print(self.name + "has slept for" + (str)(hours))

p1=person("Bob", 16, "new york", "male")
p1.eat("ice cream")
p1.sleep(5)

