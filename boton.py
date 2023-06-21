import pygame, colores

class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.medida = (x, y, ancho, alto)
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, capa):
        pygame.draw.rect(capa, colores.BLACK, self.medida)
        pygame.draw.rect(capa, colores.RED3, self.medida, 3)
        #pygame.draw.rect(screen, colores.BLACK, (x - 43, y - 8, 38, 19))
        font = pygame.font.Font(None, 36)
        texto = font.render(self.texto, True, colores.ALICEBLUE)
        texto_rect = texto.get_rect(center=self.rect.center)
        capa.blit(texto, texto_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)