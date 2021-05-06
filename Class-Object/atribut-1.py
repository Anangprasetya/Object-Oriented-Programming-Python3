# Kita gunakan class Rumah
class Rumah:

	# atribut
	index = 0

	# setiap method harus memiliki paramter self
	# method __init__ sebagai Constructor
	def __init__(self, pemilik):
		self.pemilik = pemilik
		Rumah.index += 1

	# method pada umumnya
	def katakan(self):
		print("Selamat datang di rumah",self.pemilik)

	def RumahKeBerapa(self):
		# print("Rumah ",self.pemilik, "berada di urutan ", Rumah.index, "\n")
		print(f'Rumah {self.pemilik} berada di urutan {Rumah.index} \n')





# Inisialisasi object
anang = Rumah("Anang")
anang.katakan()
anang.RumahKeBerapa()

dwi = Rumah("Dwi")
dwi.katakan()
dwi.RumahKeBerapa()

bayu = Rumah("Bayu")
bayu.katakan()
bayu.RumahKeBerapa()



"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""
