import pygame, colores, constantes, random
from disparo_enemigo import DisparoEnemigo

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes-sonido/enemy_spaceship.png").convert()
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(constantes.ancho_ventana - self.rect.width)
        self.rect.y = random.randrange(0, 200)
        self.speed_x = random.choice([-2, -1, 1, 2])

    def crear_disparo(self, total_sprites, lista_disparos_enemigos):
        self.rect.x += self.speed_x
        if self.rect.right > constantes.ancho_ventana or self.rect.left < 0:
            self.speed_x = -self.speed_x
        if random.randint(0, 100) < 1:
            self.rect.y += random.randint(1, 3)
        if random.randint(0, 100) == 0:
            enemy_bullet = DisparoEnemigo(self.rect.centerx, self.rect.bottom)
            total_sprites.add(enemy_bullet)
            lista_disparos_enemigos.add(enemy_bullet)
        
    #def crear_disparo(self, ):
        
    
    def crear_enemigo(reps, total_sprites, lista_enemigos):
        """
        Crea objetos de la clase Enemigos y los agrega a la lista de sprites.
        parametro:
        reps: El numero de Enemigos que se van a crear.
        """
        for i in range(reps):
            enemigo = Enemigo()
            total_sprites.add(enemigo)
            lista_enemigos.add(enemigo)