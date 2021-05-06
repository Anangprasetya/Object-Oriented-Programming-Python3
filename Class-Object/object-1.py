class Rumah:
	# setiap method harus memiliki paramter self

	# method __init__ sebagai Constructor
	def __init__(self, pemilik):
		self.pemilik = pemilik

	# method pada umumnya
	def katakan(self):
		print("Selamat datang di rumah",self.pemilik)





# Inisialisasi object
anang = Rumah("Anang")
anang.katakan()


bayu = Rumah("Bayu")
bayu.katakan()





"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""