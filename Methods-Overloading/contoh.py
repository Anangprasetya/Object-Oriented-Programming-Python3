
class Mobil:
	def __init__(self, nama):
		self.nama = nama

	def __del__(self):
		print("Method del")

	def __repr__(self):
		return "Method repr"

	def __str__(self):
		return "Method str"


anang = Mobil("Tesla")

print(repr(anang))
print(str(anang))
del anang