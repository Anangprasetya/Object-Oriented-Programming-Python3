class Operator:
	def __init__(self, a):
		self.a = a;


	def __str__(self):
		return "Isi var  : %d " % (self.a)

	def __add__(self, op):
		return Operator(self.a + op.a);




Coba1 = Operator(12)
print(Coba1)
Coba2 = Operator(8)
print(Coba2)

print(Coba1 + Coba2)


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""