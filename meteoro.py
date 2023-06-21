import pygame, random, constantes, colores
from funciones import getSuperficies

class Meteoro(pygame.sprite.Sprite):
    def __init__(self): #
        super().__init__()
        direccion_imagenes = ["imagenes-sonido/meteorGrey_big1.png", "imagenes-sonido/meteorGrey_big2.png", "imagenes-sonido/meteorGrey_big3.png", "imagenes-sonido/meteorGrey_big4.png", "imagenes-sonido/meteorGrey_med1.png", "imagenes-sonido/meteorGrey_med2.png", 
                                                  "imagenes-sonido/meteorGrey_small1.png", "imagenes-sonido/meteorGrey_small2.png", "imagenes-sonido/meteorGrey_tiny1.png", "imagenes-sonido/meteorGrey_tiny2.png"]
        self.image = random.choice(getSuperficies(direccion_imagenes))
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(constantes.ancho_ventana - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.velocidad_y = random.randrange(1, 10)
        self.velocidad_x = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.rect.top > constantes.alto_ventana + 10 or self.rect.left < -40 or self.rect.right > constantes.ancho_ventana + 40:
            self.rect.x = random.randrange(constantes.ancho_ventana - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 10)
    
    def reiniciar(self):
        self.rect.x = random.randrange(constantes.ancho_ventana - self.rect.width)
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