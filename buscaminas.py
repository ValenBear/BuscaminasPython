#AGREGAR SONIDO DE VICTORIA
#SI HAY DOS PUNTAJES CON EL MISMO NOMBRE, SE GUARDA EL DE MEJOR PUNTUACION
#AGREGAR SONIDO DE DERROTA


from funciones import *
from constantes import *
import pygame as pg


pg.init()   # Inicializa pygame
pantalla = pg.display.set_mode((DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
pg.display.set_caption(TITULO) # Crea el titulo del juego


#Imagenes
fondo_inicio = pg.transform.scale(pg.image.load("img/fondo-inicio.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_configuracion = pg.transform.scale(pg.image.load("img/fondo-configuracion.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_juego = pg.transform.scale(pg.image.load("img/fondo-juego.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_victoria = pg.transform.scale(pg.image.load("img/fondo-victoria.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
fondo_puntajes = pg.transform.scale(pg.image.load("img/fondo-puntajes.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
titulo = pg.transform.scale(pg.image.load("img/titulo.png"), (DIMENSIONES[ANCHO], DIMENSIONES[ALTO]))
bandera = pg.transform.scale(pg.image.load("img/bandera.png"), (DIMENSIONES[ANCHO] * 0.05, DIMENSIONES[ANCHO] * 0.05))
bomba = pg.transform.scale(pg.image.load("img/bomba.png"), (DIMENSIONES[ANCHO] * 0.05, DIMENSIONES[ANCHO] * 0.05))


#Rectangulos
rectangulo_x_centrado = (DIMENSIONES[ANCHO] // 2) - ((DIMENSIONES[ANCHO] // 4) // 2)
rectangulo_chico_x_centrado = (DIMENSIONES[ANCHO] // 2) - ((DIMENSIONES[ANCHO] // 7) // 2)
rectangulo_y_centrado = (DIMENSIONES[ALTO] // 2)
rectangulo_x_izquierda = (DIMENSIONES[ANCHO] * 0.1) - ((DIMENSIONES[ANCHO] // 4) // 2)
rectangulo_x_derecha = (DIMENSIONES[ANCHO] * 0.99) - ((DIMENSIONES[ANCHO] // 4) // 2)
rectangulo_y_up = (DIMENSIONES[ALTO] * 0.015)


#Botones Inicio
boton_jugar = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_configuracion = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.125, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_puntajes = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 2, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_salir = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + (DIMENSIONES[ALTO] * 0.125) * 3, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )


#Botones Configuracion
boton_pantalla = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )
boton_volver = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + ( + DIMENSIONES[ALTO] * 0.125) * 3, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 ) #Tambien en puntajes


#Botones Juego
boton_volver_juego = pg.Rect(rectangulo_x_izquierda, rectangulo_y_up, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_facil = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado - DIMENSIONES[ALTO] * 0.15, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_medio = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado , DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_dificil = pg.Rect(rectangulo_x_izquierda, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.15, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_reiniciar = pg.Rect(rectangulo_chico_x_centrado - DIMENSIONES[ANCHO] * 0.15, rectangulo_y_up, DIMENSIONES[ANCHO] // 7, DIMENSIONES[ALTO] // 10 )
boton_banderas = pg.Rect(rectangulo_chico_x_centrado + DIMENSIONES[ANCHO] * 0.15, rectangulo_y_up, DIMENSIONES[ANCHO] // 7, DIMENSIONES[ALTO] // 10 )
boton_timer = pg.Rect(rectangulo_x_derecha, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10)
boton_timer_victoria = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado, DIMENSIONES[ANCHO] // 6.5, DIMENSIONES[ALTO] // 10 )
boton_input = pg.Rect(rectangulo_x_centrado, rectangulo_y_centrado + DIMENSIONES[ALTO] * 0.25, DIMENSIONES[ANCHO] // 4, DIMENSIONES[ALTO] // 10 )


#Fuente
fuente = pg.font.Font(None, DIMENSIONES[ANCHO] // 25) 
fuente_puntajes = pg.font.Font(None, DIMENSIONES[ANCHO] // 30) 
fuente_titulo = pg.font.Font(None, DIMENSIONES[ANCHO] // 19)


#Textos
jugar = fuente.render("Jugar", True, NEGRO)
config = fuente.render("Configuracion", True, NEGRO)
puntajes = fuente.render("Puntajes", True, NEGRO)
salir = fuente.render("Salir", True, NEGRO)
volver = fuente.render("Volver", True, NEGRO)
texto_pantalla = fuente.render(VENTANA, True, NEGRO)
facil = fuente.render(FACIL, True, NEGRO)
medio = fuente.render(MEDIO, True, NEGRO)
dificil = fuente.render(DIFICIL, True, NEGRO)
banderas = fuente.render("0", True, NEGRO)
reiniciar = fuente.render("Reiniciar", True, NEGRO)


#Bucle Principal
corriendo = True
primer_click = False


while corriendo:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit()

        if evento.type == pg.MOUSEBUTTONDOWN:        

            if pantalla_actual == PUNTAJES_SCREEN:
                if evento.button == 1:
                    if boton_volver.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN


            elif pantalla_actual == INICIO_SCREEN:
                if evento.button == 1:
                    if boton_jugar.collidepoint(evento.pos) == True:
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        pantalla.blit(fondo_juego, (0,0))
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        pantalla_actual = JUEGO_SCREEN
                    elif boton_puntajes.collidepoint(evento.pos) == True:
                        dict_puntajes = obtener_puntajes_por_dificultad()
                        pantalla_actual = PUNTAJES_SCREEN
                    elif boton_configuracion.collidepoint(evento.pos) == True:
                        pantalla_actual = CONFIGURACION_SCREEN
                    elif boton_salir.collidepoint(evento.pos) == True:
                        pg.quit()
                        quit()
                

            elif pantalla_actual == CONFIGURACION_SCREEN:
                if evento.button == 1:
                    if boton_pantalla.collidepoint(evento.pos) == True:
                        if tipo_pantalla == FULLSCREEN: 
                            tipo_pantalla = VENTANA
                        else:
                            tipo_pantalla = FULLSCREEN                         
                        actualizar_pantalla(tipo_pantalla,pantalla,DIMENSIONES)
                        texto_pantalla = fuente.render(tipo_pantalla, True, NEGRO)
                    elif boton_volver.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN

                        
            elif pantalla_actual == JUEGO_SCREEN:
                if evento.button == 1:

                    if boton_volver_juego.collidepoint(evento.pos) == True:
                        pantalla_actual = INICIO_SCREEN
                        primer_click = False
                        tablero[DATOS][ESTADO_PARTIDA] = EN_MENU
                        reiniciar_temporizador(timers)

                    elif boton_reiniciar.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])                        
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_facil.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        dificultad = FACIL
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])                        
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_medio.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0))
                        dificultad = MEDIO
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    elif boton_dificil.collidepoint(evento.pos) == True:
                        pantalla.blit(fondo_juego, (0,0)) 
                        dificultad = DIFICIL                       
                        tablero = crear_tablero(dificultad, DIMENSIONES[ALTO])
                        tablero = dibujar_matriz(DIMENSIONES,tablero,pantalla, GRIS_CLARO, GRIS_OSCURO, NEGRO)
                        tablero[DATOS][ESTADO_PARTIDA] = JUGANDO
                        primer_click = False
                        reiniciar_temporizador(timers)

                    if tablero[DATOS][ESTADO_PARTIDA] == JUGANDO:
                        for i in range(len(tablero[MATRIZ])):
                            for j in range(len(tablero[MATRIZ][i])):
                                celda = tablero[MATRIZ][i][j]
                                if celda[RECT].collidepoint(evento.pos) == True and celda[BANDERA] == False:
                                    if primer_click == False:
                                        generar_bombas(tablero, i, j)
                                        primer_click = True
                                        timers[TIEMPO_ARRANQUE] = pg.time.get_ticks()
                                    celda[VALOR] = contar_y_revelar_celda(tablero, i , j, pantalla, GRIS_CLARO, GRIS_OSCURO, bomba)                                    
                                    if celda[VALOR] == "X":
                                        mostrar_bombas(tablero, bomba, pantalla, NEGRO, ROJO)
                                        timers[TIEMPO_DERROTA] = pg.time.get_ticks()
                                        # AGREGAR ACA SONIDO DERROTA
                                    if verificar_victoria(tablero) and primer_click:
                                        tablero[DATOS][ESTADO_PARTIDA] = VICTORIA
                                        timers[TIEMPO_VICTORIA] = pg.time.get_ticks()
                                        # AGREGAR ACA SONIDO VICTORIA

                elif evento.button == 3 and tablero[DATOS][ESTADO_PARTIDA] == JUGANDO:
                    for i in range(len(tablero[MATRIZ])):
                        for j in range(len(tablero[MATRIZ][i])):
                            celda = tablero[MATRIZ][i][j]
                            if celda[RECT].collidepoint(evento.pos) == True:
                                tablero[DATOS][BANDERAS] += poner_bandera(pantalla, celda, tablero, GRIS_OSCURO, NEGRO, bandera)   

        if evento.type == pg.KEYDOWN and tablero[DATOS][ESTADO_PARTIDA] == VICTORIA:
            if evento.key == pg.K_BACKSPACE:
                texto_ingresado = texto_ingresado[0:-1]
            elif evento.key == pg.K_RETURN:
                ganador = [texto_ingresado, dificultad, timers[TIEMPO_TRANSCURRIDO]]
                with open("puntajes.csv", "a") as puntajes_escritura:
                    texto = ",".join(str(i) for i in ganador)
                    puntajes_escritura.write(texto + "\n")
                pantalla_actual = INICIO_SCREEN
                primer_click = False
                tablero[DATOS][ESTADO_PARTIDA] = EN_MENU
                reiniciar_temporizador(timers)
                texto_ingresado = ""
            else:
                if len(texto_ingresado) < 10:
                    texto_ingresado += evento.unicode
            

    if pantalla_actual == INICIO_SCREEN:

        pantalla.blit(fondo_inicio, (0,0))
        pantalla.blit(titulo,(DIMENSIONES[ANCHO] * 0.5 - titulo.get_width() // 2, (DIMENSIONES[ALTO] * 0.5) * 0.5 - titulo.get_height() // 2))
        
        dibujar_boton(pantalla, boton_jugar, GRIS_CLARO)
        dibujar_boton(pantalla, boton_configuracion, GRIS_CLARO)
        dibujar_boton(pantalla, boton_puntajes, GRIS_CLARO)
        dibujar_boton(pantalla, boton_salir, GRIS_CLARO)

        centrar_en_boton(pantalla, jugar, boton_jugar)
        centrar_en_boton(pantalla, config, boton_configuracion)
        centrar_en_boton(pantalla, puntajes, boton_puntajes)
        centrar_en_boton(pantalla, salir, boton_salir)


    elif pantalla_actual == JUEGO_SCREEN:
        
        timer = fuente_titulo.render(str(timers[TIEMPO_TRANSCURRIDO]), True, NEGRO)
        usuario = fuente.render(str(texto_ingresado), True, NEGRO)
        
        dibujar_boton(pantalla, boton_volver_juego, GRIS_CLARO)
        dibujar_boton(pantalla, boton_facil, GRIS_CLARO)
        dibujar_boton(pantalla, boton_medio, GRIS_CLARO)
        dibujar_boton(pantalla, boton_dificil, GRIS_CLARO)
        dibujar_boton(pantalla, boton_reiniciar, GRIS_CLARO)
        dibujar_boton(pantalla, boton_banderas, GRIS_CLARO)
        dibujar_boton(pantalla, boton_timer, GRIS_CLARO)


        icono_y_texto_en_boton(pantalla, tablero, bandera, boton_banderas, NEGRO)
        centrar_en_boton(pantalla, volver, boton_volver_juego)
        centrar_en_boton(pantalla, facil, boton_facil)
        centrar_en_boton(pantalla, medio, boton_medio)
        centrar_en_boton(pantalla, dificil, boton_dificil)
        centrar_en_boton(pantalla, reiniciar, boton_reiniciar)
        centrar_en_boton(pantalla, timer, boton_timer)

        timers[TIEMPO_TRANSCURRIDO] = cronometrar_juego(timers)

        if tablero[DATOS][ESTADO_PARTIDA] == VICTORIA:
            pantalla.blit(fondo_victoria, (0,0))
            pantalla.blit(timer, (DIMENSIONES[ANCHO] // 2 - timer.get_width() // 2, DIMENSIONES[ALTO] * 0.575 - timer.get_height() // 2)) 
            boton_input = renderizar_input(usuario, DIMENSIONES)
            dibujar_boton(pantalla, boton_input, CREMA_RELLENO)
            pg.draw.rect(pantalla, CREMA_BORDE, boton_input, 2, 10)
            usuario_rect = usuario.get_rect(center=boton_input.center)
            pantalla.blit(usuario, usuario_rect)
        

    elif pantalla_actual == CONFIGURACION_SCREEN:

        pantalla.blit(fondo_configuracion, (0,0))

        dibujar_boton(pantalla, boton_pantalla, GRIS_CLARO)
        dibujar_boton(pantalla, boton_volver, GRIS_CLARO)
        centrar_en_boton(pantalla, texto_pantalla, boton_pantalla)
        centrar_en_boton(pantalla, volver, boton_volver)


    elif pantalla_actual == PUNTAJES_SCREEN:
        
        pantalla.blit(fondo_puntajes, (0,0))

        dibujar_boton(pantalla, boton_volver, GRIS_CLARO)
        centrar_en_boton(pantalla, volver, boton_volver)
        renderizar_puntajes(pantalla,fuente_puntajes,dict_puntajes,NEGRO,DIMENSIONES)

        

    pg.display.flip()
    pg.display.update()