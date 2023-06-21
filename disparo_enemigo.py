import pygame, colores, constantes

class DisparoEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("imagenes-sonido/laser1.png")
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > constantes.alto_ventana:
            self.kill()