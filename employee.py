import sys

print(sys.executable)
print(sys.version)

class Employee:
	# Sample Employee class
	def __init__(self,firstname,lastanme):
		self.firstname = firstname
		self.lastanme = lastanme

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.firstname, self.lastanme)

	@property
	def fullname(self):
		return '{} {}'.format(self.firstname, self.lastanme)

empl_1 = Employee('xavier', 'Degand')

print(empl_1.firstname)
print(empl_1.email)
print(empl_1.fullname)

