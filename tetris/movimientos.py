import matrices, bloque_aleatorio_y_niveles

class Movimientos():
	"""
	Clase que inicializa las propiedades game over, inicio, indice, lineas.
	Instancia la clase Aleatorios del módulo bloque aleatorio 
	y llama a un método para devolver bloque.
	Intancia la clase Matrices y le pasa como parámetros: el índice y el bloque,
	su color correspondiente y la lista de bloques a rellenar la matriz 
	y su lista de colores correspondiente
	"""
	def __init__(self):
		self.game_over = False
		self.inicio = True		
		self.indice = 0	
		self.lineas = 0
		self.aleatorio = bloque_aleatorio_y_niveles.Aleatorios()
		self.aleatorio.bloque_aleatorio()
		self.matriz = matrices.Matrices(self.aleatorio.bloque,
										self.aleatorio.bloque_color,
										self.aleatorio.lista_bloques, 
										self.aleatorio.lista_color_bloques,
										self.indice)		
		
########################## movimientos######################


	def recorrer_coordenadas_agrega(self, x, y):
		self.matriz.matriz_total()
		retorno = False

		for coordenada in self.aleatorio.bloque[self.indice]:
			coordenada[x] += y

			if self.chekea_limites(coordenada) == True or self.chekea_vacio(coordenada) == True:
				retorno = True
	

		if retorno == True:
			self.retornar_posicion(x, y)
			self.matriz.agrega_bloque_actual(self.indice)
			return True

		for rotacion in self.aleatorio.bloque:
			if rotacion == self.aleatorio.bloque[self.indice]:
				continue
			for coordenada in rotacion:	
				coordenada[x] += y

		self.matriz.agrega_bloque_actual(self.indice)


	def retornar_posicion(self,x, y):
		for coordenada in self.aleatorio.bloque[self.indice]:
			coordenada[x] -= y

	def mover_derecha(self):
		self.recorrer_coordenadas_agrega(1, 1)

	def mover_izquierda(self):
		self.recorrer_coordenadas_agrega(1, -1)
		
	def mover_abajo(self):
		if self.recorrer_coordenadas_agrega(0, 1):
			self.aleatorio.instanciar_proximo_bloque(self.indice)

			if self.techo():
				self.game_over = True
				self.aleatorio.pantalla_game_over()

			self.indice = 0
			self.lineas = self.matriz.eliminar_fila()
			if self.lineas > 0:
				self.aleatorio.incrementa_score(self.lineas)

			self.matriz = matrices.Matrices(self.aleatorio.bloque,
											self.aleatorio.bloque_color,
											self.aleatorio.lista_bloques, 
											self.aleatorio.lista_color_bloques, 
											self.indice)

		
	def rotar(self):
		self.matriz.matriz_total()

		if self.indice == 3:
			self.indice = 0
		else:	
			self.indice += 1
		
		self.retorna_todo()
		
	def retorna_todo(self):
		retrocede = 0
		if self.chekea_retorna_todo():
			for rotacion in self.aleatorio.bloque:
				for coordenada in rotacion:	
					if coordenada[1] == 10:
						retrocede = -1						
					elif coordenada[1] == -1:
						retrocede = 1

		for rotacion in self.aleatorio.bloque:
			for coordenada in rotacion:	
				coordenada[1] += retrocede

		if self.chekea_retorna_todo(): #Solo para el rectangulo
			for rotacion in self.aleatorio.bloque:
				for coordenada in rotacion:	
					coordenada[1] += retrocede

		self.matriz.agrega_bloque_actual(self.indice)


	def chekea_retorna_todo(self):
		for rotacion in self.aleatorio.bloque:
			for coordenada in rotacion:	
				if self.chekea_limites(coordenada) == True or self.chekea_vacio(coordenada) == True:
					return True
		

	def chekea_limites(self, coordenada):
		if coordenada[1] < 0 or coordenada[1] > 9 or coordenada[0] > 19:
			return True
		else:
			return False
		
	def chekea_vacio(self, coordenada):
		if self.matriz.matriz[coordenada[0]][coordenada[1]] != 0:
			return True
		else:
			return False
		

	def techo(self):		
		for coordenada in self.aleatorio.bloque[self.indice]:
			if self.matriz.matriz[coordenada[0]][coordenada[1]] != 0:
				return True
		