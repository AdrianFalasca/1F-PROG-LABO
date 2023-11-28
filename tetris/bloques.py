'''
Clases que contienen a las coordenadas de los bloques
y su número indicador de color
'''
class Cuadrado:
	def __init__(self):
		self.bloque = [[ [1,4], [1,5],[0,4], [0,5],],\
				[[0,4], [0,5], [1,4], [1,5]],\
				[[0,4], [0,5], [1,4], [1,5]],\
				[[0,4], [0,5], [1,4], [1,5]]]
		self.color = 1

class Rectangulo:
	def __init__(self):
		self.bloque = [[[0,5], [1,5], [2,5], [3,5]],\
				[[2,4], [2,5], [2,6], [2,7]],\
				[[0,6], [1,6], [2,6], [3,6]],\
				[[1,4], [1,5], [1,6], [1,7]]]
		self.color = 2

class Ele:
	def __init__(self):
		self.bloque = [[[0,5], [1,5], [2,5], [2,6]],\
				[[1,4], [1,5], [1,6], [0,6]],\
				[[0,4], [0,5], [1,5], [2,5]],\
				[[1,4], [1,5], [1,6], [2,4]]]
		self.color = 3

class Te:
	def __init__(self):
		self.bloque = [[[0,4], [0,5], [0,6], [1,5]],\
				[[0,4], [1,4], [1, 5], [2,4]],\
				[[1,5], [2,4], [2,5], [2,6]],\
				[[0,6], [1,5], [1,6], [2,6]]]
		self.color = 4
