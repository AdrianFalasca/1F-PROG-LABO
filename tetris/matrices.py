import pygame
import colores
color = colores.Colores()


class Matrices():
	"""
	CLase que contiene inicializa el indice, el bloque, su color correspondiente
	y la lista de bloques a rellenar la matriz y su lista de colores correspondiente.
	(Lo recibe como parámetros)
	También inicializa dos métodos para crear la matriz y otro para agregar el bloque actual.
	"""
	def __init__(self, bloque, bloque_color, lista_bloques, lista_color_bloques, indice):
		self.lista_bloques = lista_bloques
		self.lista_color_bloques = lista_color_bloques
		self.bloque_color = bloque_color
		self.bloque = bloque
		self.indice = indice

		self.matriz_total()
		self.agrega_bloque_actual(self.indice)

	def matriz_total(self):
		self.matriz = []
		self.crear_matriz()
		self.rellenar_matriz()
		

	def crear_matriz(self):
		posicion = []
		for filas in range(20):
			for columnas in range(10):
				posicion.append(0)
			self.matriz.append(posicion)
			posicion = []
		
	def rellenar_matriz(self):
		for indice, forma_ultima in enumerate(self.lista_bloques):
			for posicion in forma_ultima:
				self.matriz[posicion[0]][posicion[1]] = self.lista_color_bloques[indice]

	def eliminar_fila(self):
		lineas = 0
		for filas in enumerate(self.matriz):
			cont = 0
			for columnas in filas:
				if columnas != 0:
					cont +=1
			if cont == 10:
				lineas += 1
							
				for bloque in self.lista_bloques:
					for i in range(len(bloque)-1, -1, -1):
						if bloque[i][0] == 19:
							bloque.remove(bloque[i])
						else:
							bloque[i][0] += 1
							
		return lineas
				

	
	def agrega_bloque_actual(self, indice):
		for posicion in self.bloque[indice]:
			self.matriz[posicion[0]][posicion[1]] = self.bloque_color


	def dibujar_matriz(self, ventana):
		for filas in range(20):
			for columnas in range(10):
				numero_color = self.matriz[filas][columnas]# cambiando los colores se dibuja la forma
				pygame.draw.rect(ventana, color.lista_colores[numero_color],\
						(columnas*30+2, filas*30+5, 29, 29))
				
				
	def imprimir_matriz(self):
		print("Tetris:")
		for filas in range(20):
			for columnas in range(10):
				print(self.matriz[filas][columnas], end=" ")	
			print()
		print()



		