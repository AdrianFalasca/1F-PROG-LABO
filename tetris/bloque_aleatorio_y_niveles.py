import random
import bloques, sonidos
import pygame as pg

class Aleatorios():
	"""
	Clase que inicializa el nivel, la lista de figuras, el bloque, su color,
	lista de bloques y lista de sus colores correspondiente y el score.
	Inicializa el timer, instancia la clase sonidos y llama al método niveles.
	"""
	def __init__(self):
		self.nivel = 1
		self.lista_figuras = []
		self.bloque = []
		self.bloque_color = 0
		self.lista_bloques = []
		self.lista_color_bloques = []
		self.score = 0
	
		#####TIMER######
		self.timer = pg.USEREVENT + 0
		self.time = pg.time.set_timer(self.timer,500)

		######SONIDOS############
		self.sonidos = sonidos.Sonidos()
		self.niveles()

	def bloque_aleatorio(self):
		"""
		Método que llena la lista de figuras con las instancias de los bloques y va eliminando 
		uno a uno hasta que queda vacía y la vuelve a llenar.
		Asigna a las propiedades de bloque y color una lista y un intero.
		"""
		if len(self.lista_figuras) == 0:
			self.lista_figuras = [bloques.Te(),bloques.Ele(), bloques.Cuadrado(), bloques.Rectangulo()]

		bloque_random = random.choice(self.lista_figuras)
		self.lista_figuras.remove(bloque_random)

		self.bloque = bloque_random.bloque
		self.bloque_color = bloque_random.color


	def instanciar_proximo_bloque(self, indice):
		"""
		Método que agrega el bloque actual a la lista de bloques y el color a su lista de colores.
		Y llama al metodo para asignar otro bloque y su color
		"""
		self.lista_bloques.append(self.bloque[indice])
		self.lista_color_bloques.append(self.bloque_color)
		self.bloque_aleatorio()

############Niveles####################

	def niveles(self):
		if self.nivel == 1:
			self.sonidos.sonido_nivel1.play(-1)

		elif self.nivel == 2:
			self.sonidos.sonido_nivel1.stop()
			self.sonidos.sonido_nivel2.play(-1)
			self.time = pg.time.set_timer(self.timer,300)

			self.lista_bloques = [[[19, 0],[19, 1],[19, 2]],\
								[[18, 1],[18, 2],[17, 1]],\
								[[19, 9],[19, 8],[18, 9],[18, 8]]]
			self.lista_color_bloques = [1,2,3]

		elif self.nivel == 3:
			self.sonidos.sonido_nivel2.stop()
			self.sonidos.sonido_nivel3.play(-1)
			self.tiem = pg.time.set_timer(self.timer,100)

			self.lista_bloques = [[[19,0],[19,1],[19,2],[18,1],[18,2],[18,0]],\
					[[17,1],[17,2],[17,0],[16,0],[16,1],[19,9]],\
					[[19,8],[18,9],[18,8],[17,9],[17,8],[16,9],[16,8]],\
					[[15,8],[15,9],[14,8],[14,9],[13,8],[13,9],[12,9]]]
			self.lista_color_bloques = [1,2,3,4]

	def pantalla_game_over(self):
		self.sonidos.sonido_nivel1.stop()
		self.sonidos.sonido_nivel2.stop()
		self.sonidos.sonido_nivel3.stop()
		self.sonidos.sonido_gameover.play()

	def incrementa_score(self, lineas):
		self.score += 100 * lineas
		self.incrementa_nivel()
	
	def incrementa_nivel(self):
		if self.score == 200:
			self.nivel = 2
			self.niveles()
		elif self.score == 400:
			self.nivel = 3
			self.niveles()
        
	