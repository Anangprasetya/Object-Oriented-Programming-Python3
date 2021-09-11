class Penambahan:
	__tampung = 0

	def tambah(self):
		self.__tampung += 1

	def cetak(self):
		print("angka: %d" % (self.__tampung))

	def tambahCetak(self):
		self.tambah()
		self.cetak()

obj = Penambahan()
obj.tambah()
obj.cetak()

obj.tambahCetak()
obj.tambahCetak()
obj.tambahCetak()

# error: obj.tampung
# error: obj.__tampung
# error -> karena objek tidak mengganggap atribut itu ada atau atribut telah disembunyika dan
#          tidak dapat di akses


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""