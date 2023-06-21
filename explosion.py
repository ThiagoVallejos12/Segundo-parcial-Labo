import pygame, colores, constantes

class Explosion(pygame.sprite.Sprite):
    def __init__(self, centro, imagenes_explosion):
        super().__init__()
        self.imagenes = imagenes_explosion
        self.image = imagenes_explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.frame = 0
        self.ultima_actualizacion = pygame.time.get_ticks()
        self.velocidad = 50
    
    def update(self):
        actualizacion = pygame.time.get_ticks()
        if actualizacion - self.ultima_actualizacion > self.velocidad:
            self.ultima_actualizacion = actualizacion
            self.frame += 1
            if self.frame == len(self.imagenes):
                self.kill()
            else:
                centro = self.rect.center
                self.image = self.imagenes[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = centro

    def crear_explosion(posicion, total_sprites):
        """
        Crea una explosion en el juego en la posicion que se le indique
        parametro:
        posicion: Son las coordenadas del centro de la explosion.
        """
        imagenes_explosion = []
        for i in range(9):
            image_dir = constantes.EXPLOSIONES_IMG.format(i)
            image = pygame.image.load(image_dir)
            image.set_colorkey(colores.BLACK)
            image = pygame.transform.scale(image, (70,70))
            imagenes_explosion.append(image)
        explosion = Explosion(posicion, imagenes_explosion) #Crea un objeto de la clase Explosion con las imagenes y la posicion del centro.
        total_sprites.add(explosion) #Agrega la explosion a la lista de todos los sprites