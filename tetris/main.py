import pygame as pg
import movimientos, colores, base_datos

##### Inicialización#######		
ANCHO_VENTANA = 500
ALTO_VENTANA = 610

pg.init()
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.display.set_caption("Pygame Tetris")

jugador = ""
ingrese_nombre = False
ranking = False

########Instancias#########
mov = movimientos.Movimientos()
color = colores.Colores()
datos = base_datos.Consultas()


################Fuentes############
fuente_1 = pg.font.SysFont("Courier new", 25)
fuente_2 = pg.font.SysFont("Arial", 70)
fuente_3 = pg.font.SysFont("Arial", 15)

running = True
while running:
	############Teclas##############
	x, y = pg.mouse.get_pos()
	lista_eventos = pg.event.get()
	for evento in lista_eventos:
		if evento.type == pg.QUIT:
			running = False
			
		if ingrese_nombre == True:
				if evento.type == pg.KEYDOWN:
					if evento.key == pg.K_BACKSPACE:
						jugador = jugador[:-1]
					else:
						jugador += evento.unicode
	
							
		elif mov.game_over == False and mov.inicio == False and ranking == False:
			if evento.type == pg.USEREVENT:
				mov.mover_abajo()
				

			if evento.type == pg.KEYDOWN:
				if evento.key == pg.K_RIGHT:
					mov.mover_derecha()

				elif evento.key == pg.K_LEFT:
					mov.mover_izquierda()

				elif evento.key == pg.K_DOWN:
					mov.mover_abajo()

				elif evento.key == pg.K_SPACE:
					mov.rotar()

						

	boton_1 = pg.Rect(150, 215,200, 60)
	boton_2 = pg.Rect(150, 315,200, 60)
	boton_3 = pg.Rect(150, 415,200, 60)

	texto_jugador = fuente_1.render(f"Jugador:", True, color.NEGRO)
	texto_jugador_2 = fuente_1.render(jugador, True, color.NEGRO)
	texto_score = fuente_1.render("Score: {}".format(mov.aleatorio.score), True, color.NEGRO)
	texto_nivel = fuente_1.render("Nivel: {}".format(mov.aleatorio.nivel), True, color.NEGRO)
	texto_salir = fuente_1.render("Salir", True, color.NEGRO)

	ventana.fill(color.GRIS) 

	#############Pantalla de inicio#########
	if mov.inicio == True:
		if boton_1.collidepoint((x,y)):
			ingrese_nombre = True
			mov.inicio = False
		elif boton_2.collidepoint((x,y)):
			ranking = True
			mov.inicio = False
			
		elif boton_3.collidepoint((x,y)):
			running = False

		pg.draw.rect(ventana, color.OTRO_AZUL, boton_1, border_radius=10)
		pg.draw.rect(ventana, color.OTRO_AZUL, boton_2, border_radius=10)
		pg.draw.rect(ventana, color.OTRO_AZUL, boton_3, border_radius=10)	
		
		texto_tetris = fuente_2.render("Tetris", False, color.NEGRO)
		texto_jugar = fuente_1.render("Jugar", True, color.NEGRO)
		texto_ranking = fuente_1.render("Ranking", True, color.NEGRO)

		ventana.blit(texto_tetris,(160,40))
		ventana.blit(texto_jugar,(200,230))
		ventana.blit(texto_ranking,(195,330))
		ventana.blit(texto_salir,(200,430))
		
		################Pantalla para ingresar nombre#########
	elif ingrese_nombre == True:
			if boton_3.collidepoint((x,y)) and jugador != "":
				ingrese_nombre = False
				
			datos_partida = pg.Rect(10, 200, 480, 100)
			input_jugador = pg.Rect(280, 220, 200, 30)

			pg.draw.rect(ventana, color.NEGRO, datos_partida, width=3, border_radius=10)
			pg.draw.rect(ventana, color.BLANCO, input_jugador,width=1, border_radius=10)
			pg.draw.rect(ventana, color.OTRO_AZUL, boton_3, border_radius=10)

			texto_tetris = fuente_2.render("Tetris", False, color.NEGRO)
			texto_jugar = fuente_1.render("Jugar", True, color.NEGRO)
			texto_ingrese_nombre = fuente_1.render(f"Ingrese su nombre {jugador}", True, color.NEGRO)

			ventana.blit(texto_tetris,(160,40))
			ventana.blit(texto_ingrese_nombre,(15,220))
			ventana.blit(texto_jugar,(200,430))

	############Pantalla del ranking#############
	elif ranking == True:
			boton_3 = pg.Rect(150, 515,200, 60)
			if boton_3.collidepoint((x,y)):
				mov.inicio = True
				ranking = False
				
			recuadro_datos_partida = pg.Rect(10, 200, 480, 300)
		
			pg.draw.rect(ventana, color.NEGRO, recuadro_datos_partida, width=3, border_radius=10)
			pg.draw.rect(ventana, color.OTRO_AZUL, boton_3, border_radius=10)

			texto_tetris = fuente_2.render("Tetris", False, color.NEGRO)
			texto_inicio = fuente_1.render("Inicio", True, color.NEGRO)

			y = 220
			contador = 1
			cursor = datos.traer_datos()
			for fila in cursor:
				texto_nombre_score = fuente_1.render(f"{contador}.Jugador: {fila[1]}, Score: {fila[2]}", True, color.NEGRO)
				ventana.blit(texto_nombre_score,(15,y))
				y += 50
				contador += 1

			ventana.blit(texto_tetris,(160,40))
			ventana.blit(texto_inicio,(200,530))

	#############Pantalla de game over#############
	elif mov.game_over == True:
		if boton_2.collidepoint((x,y)):
			mov.inicio = True
			datos.agregar_dato(jugador, mov.aleatorio.score)
			mov = movimientos.Movimientos()
		elif boton_3.collidepoint((x,y)):
			datos.agregar_dato(jugador, mov.aleatorio.score)
			running = False

		
		datos_partida = pg.Rect(100, 200, 300, 100)	

		pg.draw.rect(ventana, color.OTRO_AZUL, boton_2, border_radius=10)
		pg.draw.rect(ventana, color.OTRO_AZUL, boton_3, border_radius=10)	
		pg.draw.rect(ventana, color.NEGRO, datos_partida, width=3, border_radius=10)
		
		texto_gameover = fuente_2.render("GAME OVER", False, color.NEGRO)
		texto_ir_inicio = fuente_1.render("Inicio", True, color.NEGRO)

		ventana.blit(texto_gameover,(75,40))
		ventana.blit(texto_ir_inicio,(195,330))
		ventana.blit(texto_salir,(200,430))
		ventana.blit(texto_score,(110,250)) 
		ventana.blit(texto_jugador,(110,205))
		ventana.blit(texto_jugador_2,(235,205))
		
	#############Pantalla del juego##############	
	else:
		cronometro = 200 - (pg.time.get_ticks() // 1000)
		text_tiempo = fuente_1.render("Tiempo: "+ str(cronometro), True, color.NEGRO)
		if cronometro < 0:
			mov.game_over = True	
			mov.aleatorio.pantalla_game_over()
		
		input_jugador = pg.Rect(310, 8, 185, 150)
		pg.draw.rect(ventana, color.OTRO_AZUL, input_jugador, width=3, border_radius=10)
		mov.matriz.dibujar_matriz(ventana)
		ventana.blit(texto_nivel,(320,20))
		ventana.blit(texto_score,(320,50)) 
		ventana.blit(texto_jugador,(320,80))
		ventana.blit(texto_jugador_2,(320,110))
		ventana.blit(text_tiempo,(310,550)) 

	pg.display.flip()



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
	
