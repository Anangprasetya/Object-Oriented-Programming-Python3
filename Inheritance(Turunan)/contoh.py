
class OrangTua:
	harta = 20
	def __init__(self):
		print("Sebagai Orang Tua")

	def syarat(self):
		print(f'Jika bisa menjadi anak yang baik maka akan di beri warisan sebesar {OrangTua.harta}')


class Anak(OrangTua):
	def __init__(self):
		print("Sebagai Anak")


	def terima(self):
		print("Saya akan menjadi harta warisan ini !")

a = Anak()
a.terima()

a.syarat()




"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""