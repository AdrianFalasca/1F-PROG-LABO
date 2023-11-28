import pygame as pg

class Sonidos():
    def __init__(self):
        self.sonido_nivel1 = pg.mixer.Sound("musica/nivel1.ogg")
        self.sonido_nivel2 = pg.mixer.Sound("musica/nivel2.ogg")
        self.sonido_nivel3 = pg.mixer.Sound("musica/nivel3.ogg")
        self.sonido_gameover = pg.mixer.Sound("musica/gameover.mp3")