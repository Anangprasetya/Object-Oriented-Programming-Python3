
class Antrian:
	index = 0

	def __init__(self, nama, usia):
		self.nama = nama
		self.usia = usia
		Antrian.index += 1

	def totalAtrian(self):
		print("Total antrian %d" % Antrian.index)

	def pelaku(self):
		print ("Nama : ", self.nama, ", Usia : ", self.usia)



print("Antrian.doc : ", Antrian.__doc__)
print("Antrian.name : ", Antrian.__name__)
print("Antrian.module : ", Antrian.__module__)
print("Antrian.bases : ", Antrian.__bases__)
print("Antrian.dict : ", Antrian.__dict__)


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""