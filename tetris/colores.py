class Colores():
    """
    Clase que inicializa las propiedades con los colores y una lista 
    que los contiene.
    """
    def __init__(self):
        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        self.ROJO = (255, 0, 0,)
        self.VERDE = (0, 255, 0)
        self.AZUL = (0, 0, 255)
        self.NARANJA = (255, 128, 0)
        self.GRIS = (125, 125, 125)
        self.OTRO_AZUL = (5, 76, 109)

        self.lista_colores = [self.NEGRO, self.ROJO, self.VERDE, self.AZUL, self.NARANJA]