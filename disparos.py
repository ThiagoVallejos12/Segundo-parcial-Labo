import pygame, colores, constantes
class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(constantes.DISPARO_JUGADOR_IMG)
        self.image = pygame.transform.flip(self.image, False, True)
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidad_y = -10
    
    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom < 0:
            self.kill()
