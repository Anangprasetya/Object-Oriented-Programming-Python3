
class Mobil:
	# method init bertindak sebagai constructor 
	def __init__(self, warna):
		self.warna = warna
		print("Membuat objek")


	# method del bertindak sebagai destructor
	def __del__(self):
		print("Object mobil,", self.warna, " dihapus")


pajero = Mobil("Merah")
avanza = Mobil("Putih")


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""