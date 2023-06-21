import pygame, constantes, colores
from disparos import Disparo

class Jugador(pygame.sprite.Sprite):#Define la clase jugador que hereda todos los atributos y metodos de la clase base Sprite.
                                    #Esto incluye el uso de grupos de sprites para facilitar la gestión y la detección de colisiones entre los objetos del juego.
                                    #Se utiliza la superclase Sprite para aprovechar las funcionalidades y ventajas proporcionadas por dicha clase al trabajar con sprites. 
                                    #Ej: Gestion de grupos de sprites. Mas que nada para la realizar operaciones de dibujo y actualizacion en todos los sprites de un grupo de forma simultanea.
    
    def __init__(self): #Constructor clase jugador
        super().__init__() #Se ejecuta el constructor de la clase Sprite(clase base) antes de hacer cualquier otra inicializacion de la clase jugador
        self.image = pygame.image.load("imagenes-sonido/player.png").convert()
        self.image.set_colorkey(colores.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = constantes.ANCHO_VENTANA / 2
        self.rect.bottom = constantes.ALTO_VENTANA - 10
        self.velocidad_x = 0
        self.escudo = 100

    def update(self): #Actualiza la posicion del jugador en cada fotograma del juego.
        self.velocidad_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocidad_x = -5
        if keys[pygame.K_RIGHT]:
            self.velocidad_x = 5
        self.rect.x += self.velocidad_x
        if self.rect.right > constantes.ANCHO_VENTANA:
            self.rect.right = constantes.ANCHO_VENTANA
        if self.rect.left < 0:
            self.rect.left = 0

    def reiniciar(self): #Reinicia la posicion y los atributos del jugador.
        self.rect.centerx = constantes.ANCHO_VENTANA / 2
        self.rect.bottom = constantes.ALTO_VENTANA - 10
        self.velocidad_x = 0
        self.escudo = 100

    def disparar(self,total_sprites,lista_disparos): #Crea una instancia de la clase disparo
        tiro = Disparo(self.rect.centerx, self.rect.top)
        total_sprites.add(tiro)
        lista_disparos.add(tiro)

    def crear_jugador(total_sprites,personaje_lista):
        """
        Crea un objeto de la clase jugador y lo agrega a la lista de sprites.
        Retorno:
        jugador: el objeto de jugador creado.
        """
        jugador = Jugador()
        total_sprites.add(jugador)
        personaje_lista.add(jugador)
        return jugador