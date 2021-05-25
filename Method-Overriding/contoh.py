
class Mobil:
	def warna(self):
		print("Mobil x memiliki warna merah")


class Xenia(Mobil):
	def warna(self):
		print("Mobil Xenia memiliki warna hitam")


# Overriding digunakan untuk mengganti method induknya

a = Xenia()
a.warna()


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""