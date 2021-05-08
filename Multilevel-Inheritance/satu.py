
class Komputer:
	jenis = "Laptop"
	def __init__(self, nama, harga):
		self.nama = nama
		self.harga = harga

	def deskripsi(self):
		return f'{self.nama} memiliki harga Rp. {self.harga}'

	def warna(self, warna):
		return f'{Komputer.jenis} {self.nama} memiliki warna {warna}'


class Umum(Komputer):
	def kegunaan(self, guna):
		return f'{Komputer.jenis} {self.nama} bisa digunakan {guna}'


class Gaming(Komputer):
	def kegunaan(self, guna):
		return f'{Komputer.jenis} {self.nama} bisa digunakan {guna}'



game = Gaming("Acer", 20000)
print(game.deskripsi())
print(game.warna("hitam"))
print(game.kegunaan("Bermain Game"))


print("\n")


semua = Umum("HP", 30000)
print(semua.deskripsi())
print(semua.warna("Merah"))
print(semua.kegunaan("Keperluan pada umumnya"))


"""
==========================================================
==================  Versi Python 3.8.5  ==================
==================        2021          ==================
==========================================================
"""