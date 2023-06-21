import pygame, constantes, colores, sqlite3
from funciones import *
from sql import *
from jugador import Jugador
from meteoro import Meteoro
from enemigo import Enemigo
from explosion import Explosion
from pygame.locals import *
from boton import Boton

class Juego:
    def __init__(self):
        self.total_sprites = pygame.sprite.Group()
        self.lista_enemigos = pygame.sprite.Group()
        self.lista_meteoros = pygame.sprite.Group()
        self.lista_disparos = pygame.sprite.Group()
        self.lista_disparos_enemigos = pygame.sprite.Group()
        self.personaje_lista = pygame.sprite.Group()

        self.pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
        pygame.display.set_caption("Alien Space")
        self.reloj = pygame.time.Clock()

        self.titulo = pygame.image.load("imagenes-sonido/titulojuego.png")
        self.fondo_gameover = pygame.image.load("imagenes-sonido/game_over1.jpg")
        self.fondo_menus = pygame.image.load("imagenes-sonido/fondo2.png")
        self.fondo_ingame = pygame.image.load("imagenes-sonido/fondo1.png")

    def reiniciar_juego(self):
        """
        Reinicia el juego al estado inicial.
        parametro:
        jugador: El objeto del jugador a reiniciar.
        """
        self.total_sprites.empty() #Se eliminan todos los sprites
        self.lista_meteoros.empty() #Se eliminan todos los meteoros, disparos y enemigos de sus respectivas listas.
        self.lista_disparos.empty()
        self.lista_disparos_enemigos.empty()
        self.lista_enemigos.empty()

        self.jugador.reiniciar() #Reinicia las propiedades del jugador.

    def game_over(self):
        """
        Muestra la pantalla de Game Over y da la posibilidad al jugador de volver al menu principal.
        parametros:
        jugador: objeto que representa al jugador.
        pantalla: la superficie donde se van a dibujar.
        fondo: imagen de fondo que se mostrara al finalizar el juego.
        """
        self.objeto.reiniciar_juego() #Reinicia el juego para prepararlo para una nueva partida.
        self.fondo_gameover.set_alpha(0)
        boton_salir = Boton(constantes.ANCHO_VENTANA/2-125, 550, 250, 50, 'VOLVER AL MENU')
        run = True
        flag = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_salir.is_clicked(pygame.mouse.get_pos()):
                        run = False
            if flag:            
                for alpha in range(0, 100):  #Rango de 0 a 100 para aumentar gradualmente la transparencia.
                    self.fondo_gameover.set_alpha(alpha * 2.55)  #Establece el nivel de transparencia en cada iteración.
                    self.pantalla.blit(self.fondo_gameover, (0, 0))  #Dibuja la superficie negra en la pantalla.
                    pygame.display.flip()  #Actualiza la pantalla.
                    pygame.time.wait(10) #Espera 10 milis.
                flag = False #Se cambia a false para no repetir la animacion.

            boton_salir.dibujar(self.pantalla)
            pygame.display.flip()

    def pedir_nombre(self):
        """
        Muestra una pantalla donde el jugador puede ingresar su nombre.

        parametros:
        pantalla: la superficie donde se van a dibujar.
        ancho: ancho de la pantalla.
        fondo: imagen de fondo que se mostrara mientras ingresa el nombre.
        titulo: texto que representa el titulo del juego que se muestra en el centro de la pantalla.

        retorno:
        entrada: Es el nombre que el jugador ingreso.
        """
        pygame.font.init()
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Ingrese su nombre:", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(constantes.ANCHO_VENTANA / 2, 370))
        fondo_rect = self.fondo_menus.get_rect()
        titulo_rect = self.titulo.get_rect()
        titulo_rect.center = (constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2) #posiciona el título en el centro
        titulo_rect.y = 50
        alpha = 0

        entrada = "" #esta cadena va a almacenar el nombre que se vaya a ingresar.
        entrada_rect = pygame.Rect(constantes.ANCHO_VENTANA/2-100, 400, 200, 40)
        activo = True
        while activo:
            fondo_rect.y += 1
            fondo_rect.y %= fondo_rect.height
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN:
                    if event.key == K_RETURN: #verifica si se presiona enter
                        activo = False
                    elif event.key == K_BACKSPACE: #si se presiona la tecla para borrar, elimina el último carácter de la entrada.
                        entrada = entrada[:-1]
                    elif event.key == K_ESCAPE: #verifica si se presiona escape
                        pygame.quit()
                        return #sale del bucle principal
                    else:
                        entrada += event.unicode #Agrega el carácter ingresado a la cadena creada anteriormente.
        
            entrada_superficie = fuente.render(entrada, True, (255, 255, 255))
            entrada_rect.w = max(200, entrada_superficie.get_width() + 10)
            self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y - fondo_rect.height))
            self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y))
            pygame.draw.rect(self.pantalla, colores.BLACK, entrada_rect)
            pygame.draw.rect(self.pantalla, colores.RED3, entrada_rect, 3)
            self.pantalla.blit(texto, texto_rect)
            self.pantalla.blit(entrada_superficie, (entrada_rect.x + 5, entrada_rect.y + 5))
            while alpha < 255:
                self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y - fondo_rect.height))
                self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y))
                self.titulo.set_alpha(alpha)
                self.pantalla.blit(self.titulo, titulo_rect)
                pygame.display.flip()
                pygame.time.delay(10)
                alpha += 10 #Incrementa la transparencia del título
            self.pantalla.blit(self.titulo, titulo_rect)
            pygame.display.flip()
        return entrada

    def mostrar_marcadores(self):
        """
        Muestra la tabla de puntuaciones en la pantalla.

        parametros:
        pantalla: la superficie donde se van a dibujar.
        fondo: imagen de fondo mientras se muestra la tabla de puntuaciones.
        retorno:
        None: En caso de que ocurrar algun error durante la ejecucion.
        """
        try:
            with sqlite3.connect("puntuaciones.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT nombre, puntuacion FROM jugadores ORDER BY puntuacion DESC")
                puntuaciones = cursor.fetchall()
                print(puntuaciones)
            boton = Boton(constantes.ANCHO_VENTANA-250, 200, 200, 50, 'VOLVER')
            self.pantalla.blit(self.fondo_menus, (0, 0))
            fuente = pygame.font.Font(None, 30)
            pygame.draw.rect(self.pantalla, colores.GRAY15,(440, 110, 440, 500)) #Rectangulo donde se mostraran las puntuaciones.
            pygame.draw.rect(self.pantalla, colores.RED3,(440, 110, 440, 500), 5)
            x = 480
            y = 180
            texto = "Tabla de puntuaciones:"
            texto1 = "Nombre"
            texto2 = "Puntuacion"
            r_texto = fuente.render(texto, True, (255, 255, 255), colores.VIOLETRED)
            r_texto1 = fuente.render(texto1, True, (255, 255, 255), colores.VIOLETRED)
            r_texto2 = fuente.render(texto2, True, (255, 255, 255), colores.VIOLETRED)
            self.pantalla.blit(r_texto, (x, y - 60)), self.pantalla.blit(r_texto1, (x, y - 30)), self.pantalla.blit(r_texto2, (x + 220, y - 30))
            for datos in puntuaciones: #Dibuja todos los nombres y puntuaciones en el rectangulo que se dibujo anteriormente.
                nombre = datos[0]
                puntuacion = datos[1]
                render_nombre = fuente.render(str(nombre), True, (255, 255, 255))
                render_puntuacion = fuente.render(str(puntuacion), True, (255, 255, 255))
                self.pantalla.blit(render_nombre, (x, y)), self.pantalla.blit(render_puntuacion, (x + 220, y))
                y += 30
            boton.dibujar(self.pantalla) 
            pygame.display.flip()
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if boton.is_clicked(pygame.mouse.get_pos()):
                            run = False
        except:
            return None

    def iniciar_juego(self):
        """
        Inicia el juego.
        parametros:
        pantalla: la superficie donde se van a dibujar.
        nombre_jugador: nombre del jugador.
        """
        try:
            sonido_explosion = pygame.mixer.Sound("imagenes-sonido/assets_explosion.wav")
            sonido_golpe = pygame.mixer.Sound("imagenes-sonido/uhsteve.wav")
            sonido_laser = pygame.mixer.Sound("imagenes-sonido/laser5.ogg")
            sonido_golpe.set_volume(0.1), sonido_explosion.set_volume(0.1), sonido_laser.set_volume(0.3)
        except pygame.error as e:
            print("Error al cargar los archivos de imagen o sonido:", str(e))
            pygame.quit()
        self.jugador = Jugador.crear_jugador(self.total_sprites, self.personaje_lista) #Crea el jugador
        run = True
        fondo_rect = self.fondo_ingame.get_rect()
        puntuacion = 0
        Meteoro.crear_meteoro(4, self.total_sprites, self.lista_meteoros) #Se crea la cantidad de meteoros y enemigos que se ingresen por parametro.
        Enemigo.crear_enemigo(8, self.total_sprites, self.lista_enemigos)
        while run:
            fondo_rect.y += 1
            fondo_rect.y %= fondo_rect.height
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sonido_laser.play()
                        self.jugador.disparar(self.total_sprites, self.lista_disparos)
            
            #Enemigo.crear_disparo(total_sprites, lista_disparos_enemigos)
            self.total_sprites.update() #Actualiza todos los sprites en el juego.

            for enemigo in self.lista_enemigos:
                enemigo.crear_disparo(self.total_sprites, self.lista_disparos_enemigos)
        
            colision1 = pygame.sprite.groupcollide(self.lista_enemigos, self.lista_disparos, True, True) #Se verifican colisiones entre enemigos y disparos del jugador
            colision2 = pygame.sprite.groupcollide(self.lista_disparos_enemigos, self.lista_disparos, True, True) #Se verifican colisiones entre disparos enemigos y disparos del jugador
            colision3 = pygame.sprite.groupcollide(self.lista_meteoros, self.lista_disparos, True, True) #Se verifican colisiones entre meteoros y disparos del jugador
            
            if colision1:
                for i in colision1:
                    Explosion.crear_explosion(i.rect.center, self.total_sprites)
                    sonido_explosion.play()
                    Enemigo.crear_enemigo(1, self.total_sprites, self.lista_enemigos)
                    puntuacion += 10
            if colision2:
                for i in colision2:
                    Explosion.crear_explosion(i.rect.center, self.total_sprites)
                    sonido_explosion.play()
                    puntuacion += 5
            if colision3:
                for i in colision3:
                    Explosion.crear_explosion(i.rect.center, self.total_sprites)
                    sonido_explosion.play()
                    Meteoro.crear_meteoro(1, self.total_sprites, self.lista_meteoros)
                    puntuacion += 20

            choques_disparos_jugador = pygame.sprite.spritecollide(self.jugador, self.lista_disparos_enemigos, True) #Se verifican colisiones entre el jugador y disparos enemigos
            choque_meteoro_jugador = pygame.sprite.spritecollide(self.jugador, self.lista_meteoros, True) #Se verifican colisiones entre el jugador y los meteoros
            if choques_disparos_jugador or choque_meteoro_jugador:
                sonido_golpe.play()
                self.jugador.escudo -= 25
                if choque_meteoro_jugador:
                    Meteoro.crear_meteoro(1, self.total_sprites, self.lista_meteoros)
                if self.jugador.escudo <= 0:
                    run = False
                    guardar_puntuacion(self.nombre_jugador, int(puntuacion), "puntuaciones.db")
                    self.objeto.game_over()
                    #reiniciar_juego(jugador)
            
            self.pantalla.blit(self.fondo_ingame, (0, fondo_rect.y - fondo_rect.height))
            self.pantalla.blit(self.fondo_ingame, (0, fondo_rect.y))
            self.total_sprites.draw(self.pantalla)
            dibujar_texto(self.pantalla, str(puntuacion), 25, constantes.ANCHO_VENTANA // 2, 10)
            dibujar_barra_escudo(self.pantalla, constantes.ANCHO_VENTANA - 155, constantes.ALTO_VENTANA - 25, self.jugador.escudo)
            pygame.display.flip()

    def main(self, juego):
        """
        Funcion principal del juego.
        """
        self.objeto = juego
        try:
            self.titulo = pygame.transform.scale(self.titulo, (720, 100))
            titulo_rect = self.titulo.get_rect()
            titulo_rect.center = (constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2)
            titulo_rect.y = 50
            fondo_rect = self.fondo_menus.get_rect()
            pygame.mixer.music.load("imagenes-sonido/music.ogg")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(loops=-1) #reproduce la musica en bucle.
        except pygame.error as e:
            print("Error al cargar los archivos de imagen o sonido:", str(e))
            pygame.quit()

        self.nombre_jugador = juego.pedir_nombre() #Se ejecuta el menu de la funcion pedir_nombre.
        
        boton_play = Boton(constantes.ANCHO_VENTANA/2-100, 300, 200, 50, 'Jugar')
        boton_marcadores = Boton(constantes.ANCHO_VENTANA/2-100, 400, 200, 50, 'Scoreboard')

        while True:
            milis = self.reloj.tick(60)
            fondo_rect.y += 1
            fondo_rect.y %= fondo_rect.height
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_play.is_clicked(pygame.mouse.get_pos()):
                        crear_tabla("imagenes-sonido/puntuaciones.db") #Crea una tabla en la base de datos para las puntuaciones si no existe
                        juego.iniciar_juego() #Inicia el juego
                        print("Iniciar juego")
                    elif boton_marcadores.is_clicked(pygame.mouse.get_pos()):
                        juego.mostrar_marcadores() 
                        print("Mostrar mejores puntuaciones")

            self.pantalla.fill((0, 0, 0))
            self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y - fondo_rect.height))
            self.pantalla.blit(self.fondo_menus, (0, fondo_rect.y))
            self.pantalla.blit(self.titulo, titulo_rect)
            boton_play.dibujar(self.pantalla)
            boton_marcadores.dibujar(self.pantalla)
            pygame.display.flip()

