
print("----Python Program Practice----");

print("Demonstration of Behaviour of class");

class Demo:
	def __init__(self):
		self.i=0;
		self.j=0;

	def fun(self):
		print("Inside instance method");

	@classmethod
	def sun(cls):
		print("Inside Class method");

	@staticmethod
	def gun():
		print("Inside static method");

obj1=Demo();
obj1.fun();
obj1.gun();
obj1.sun();


####//////////////////////////////////////////////////////////////////////
### Output:
##	----Python Program Practice----
##	Demonstration of Behaviour of class
##	Inside instance method
##	Inside static method
##	Inside Class method
###////////////////////////////////////////////////////////////////////////			
