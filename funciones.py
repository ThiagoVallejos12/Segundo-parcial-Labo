import pygame, colores
from pygame.locals import *

#Funciones auxiliares
def getSuperficies(direcciones)-> list:
    """
    Carga y devuelve una lista con imagenes.
    
    direcciones: Las rutas de la imagen a cargar.
    Retorno:
    Imagenes: una lista de imagenes.
    """
    imagenes = []
    for i in direcciones:
        imagenes.append(pygame.image.load(i)) #Carga la imagen de cada ruta de archivo y la agrega a la lista de superficies
    return imagenes

"""def cargar_imagen(ruta):
    try:
        imagen = pygame.image.load(ruta)
        return imagen
    except pygame.error as e:
        print("Error al cargar la imagen:", str(e))
        pygame.quit()"""

def cargar_sonido(ruta, volumen):
    """
    Carga un sonido y le da un volumen.
    parametros:
    ruta: la ruta del archivo de sonido.
    volumen: valor decimal entre 0 y 1 que va a ser el volumen del sonido
    retorno:
    sonido: el objeto de sonido cargado.
    """
    try:
        sonido = pygame.mixer.Sound(ruta) 
        sonido.set_volume(volumen)
        return sonido
    except pygame.error as e:
        print("Error al cargar el sonido:", str(e))
        pygame.quit()

def dibujar_texto(pantalla, texto, tamaño, x, y):
    """
    Dibuja un texto en la pantalla.
    parametros:
    pantalla: Donde se dibujara el texto.
    texto: El texto a dibujar
    tamaño: tamaño de la fuente del texto
    x: posicion x en donde se ubicara el texto
    y: posicion y en donde se ubicara el texto
    """
    fuente = pygame.font.SysFont("serif", tamaño)
    capa_texto = fuente.render(texto, True, colores.WHITE)
    texto_rect = capa_texto.get_rect()
    texto_rect.midtop = (x, y)
    pantalla.blit(capa_texto, texto_rect)

def dibujar_barra_escudo(pantalla, x, y, escudo):
    """
    Dibuja la barra de escudo en la pantalla
    parametros:
    pantalla: Donde se dibujara la barra de escudo
    x: la coordenada x en donde se empezara a dibujar la barra de escudo
    y: la coordenada y en donde se empezara a dibujar la barra de escudo
    escudo: el valor de escudo actual, entre 0 y 100
    """
    barra_lenght = 150
    barra_height = 20
    relleno_barra = (escudo / 100) * barra_lenght
    borde_barra = pygame.Rect(x, y, barra_lenght, barra_height)
    relleno_barra = pygame.Rect(x, y, relleno_barra, barra_height)
    pygame.draw.rect(pantalla, colores.RED3, relleno_barra) #dibuja el relleno de la barra de escudo
    pygame.draw.rect(pantalla, colores.GREENYELLOW, borde_barra, 2) #dibuja el borde de la barra de escudo
    pygame.draw.rect(pantalla, colores.RED3, (x - 45, y -2, 42, 23)) 
    pygame.draw.rect(pantalla, colores.BLACK, (x - 43, y, 38, 19))
    dibujar_texto(pantalla, str(escudo), 24, x - 25, y -5)

