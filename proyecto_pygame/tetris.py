import pygame
import random

ANCHO_VENTANA = 300
ALTO_VENTANA = 600

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pygame Tetris")
running = True
coordenada_x = 150
coordenada_y = 0

timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,500)

def formas(coordenada_x, coordenada_y):
	lista_formas = [(coordenada_x, coordenada_y, 60, 60),\
					(coordenada_x, coordenada_y, 30, 120),\
					[(coordenada_x, coordenada_y, 30, 90),(coordenada_x, coordenada_y+60, 60, 30)],\
					[(coordenada_x+30, coordenada_y, 30, 60),(coordenada_x, coordenada_y, 90, 30)]]
	
	indice_random = random.randrange(1)
	return lista_formas[indice_random]



while running:
	
	lista_eventos = pygame.event.get()
	for evento in lista_eventos:
		if evento.type == pygame.QUIT:
			running = False

		if evento.type == pygame.USEREVENT:
			if coordenada_y + lista_formas[3] == 600:
				#llamar a otra forma
				coordenada_y = 0
				coordenada_x = 150
			else:
				coordenada_y += 30
				
		if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_RIGHT:
				if coordenada_x + lista_formas[2] != 300:
					coordenada_x += 30
			elif evento.key == pygame.K_LEFT:
				if coordenada_x != 0:
					coordenada_x -= 30

			elif evento.key == pygame.K_DOWN:
				if coordenada_y + lista_formas[3] == 600:
					#llamar a otra forma
					coordenada_y = 0
					coordenada_x = 150
				else:
					coordenada_y += 60


	ventana.fill((0, 0, 0)) # Se pinta el fondo de la ventana

	lista_formas = formas(coordenada_x, coordenada_y)
	pygame.draw.rect(ventana, (125, 125, 125), lista_formas)

	pygame.display.flip()# Muestra los cambios en la pantalla
	# ventana.blit()# para actualizar
	"""
TEMA: TETRIS
Descripción
El juego deberá permitir a los jugadores controlar la caída y la rotación de bloques para crear
líneas horizontales completas y ganar puntos. El jugador puede mover el bloque en la zona de
juego sin salir de los límites de la pantalla. Deberá aparecer el puntaje del jugador y el nombre
del mismo.
Requisitos del Juego:
Pantalla de Inicio:
Debe haber una pantalla de inicio con un título y botones para comenzar el juego, ver las
opciones y salir del mismo. En la cual, se deberá ingresar el nombre del jugador, este NO
puede ser por consola, sino en la misma pantalla.
Jugador Principal:
El jugador debe controlar el bloque que aparezca en pantalla, que puede moverlo en el
espacio de juego de forma limitada, para la derecha o izquierda.
Niveles:
El juego debe contar con 3 niveles distintos, cada uno debe agregar una dificultad respecto al
nivel anterior (más enemigos, objetos que se mueven a mayor velocidad, etc).
Tipos de bloques:
Los bloques solamente deberán ser de 4 formas:

● Rectángulo
● Cuadrado
● Forma de T
● Forma de L
Modalidad del juego:

Cada bloque deberá aparecer de manera aleatoria, es decir no debe haber un orden entre un
tipo de elemento y el que le sigue.
Cada partida debe ser por tiempo o hasta no poder realizarse más movimientos.
Mientras el bloque va bajando, no se puede volver a subir. Una vez que bajó totalmente no se
puede mover hacia ningún lado.
Al final de cada partida se deberá guardar el SCORE junto con el nombre de usuario. En tal
sentido, se deberá elaborar un ranking ordenado de mayor a menor puntuación, mostrando
su respectivo nombre y puntuación
Tiempo:
Tiene que contar con un cronómetro.
Score:
Tiene que contar con un SCORE, el cual debe ser guardado utilizando bases de datos una
vez finalizado el juego. Solamente será necesario utilizar una tabla, donde se guardará el
nombre de usuario y el score.
El juego debe contar con una pantalla que permita visualizar un TOP 5 de los mejores
puntajes guardados.
Pantalla de Fin:
Cuando el jugador pierde todas sus vidas, se debe mostrar una pantalla de fin que muestre la
puntuación final del jugador.
	"""
	
