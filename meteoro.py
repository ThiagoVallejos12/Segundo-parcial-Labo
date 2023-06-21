import pygame, random, constantes, colores
from funciones import getSuperficies

class Meteoro(pygame.sprite.Sprite):
    def __init__(self): #
        super().__init__()
        direccion_imagenes = constantes.METEOROS_IMG
        self.image = random.choice(getSuperficies(direccion_imagenes))
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(constantes.ANCHO_VENTANA - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.velocidad_y = random.randrange(1, 10)
        self.velocidad_x = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.rect.top > constantes.ALTO_VENTANA + 10 or self.rect.left < -40 or self.rect.right > constantes.ANCHO_VENTANA + 40:
            self.rect.x = random.randrange(constantes.ANCHO_VENTANA - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 10)
    
    def reiniciar(self):
        self.rect.x = random.randrange(constantes.ANCHO_VENTANA - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
    
    def crear_meteoro(reps, total_sprites, lista_meteoros):
        """
        Crea objetos de la clase Metoro y los agrega a la lista de sprites.
        parametro:
        reps: El numero de meteoros que se van a crear.
        """
        for i in range(reps):
            meteoro = Meteoro()
            total_sprites.add(meteoro)
            lista_meteoros.add(meteoro)