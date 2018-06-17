#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# andando02.py
# Movimiento con controles propios
#-----------------------------------------------------------------------
import pilasengine

pilas=pilasengine.iniciar()

# Definimos las teclas que moverán al personaje
teclas = {pilas.simbolos.a:"izquierda", pilas.simbolos.s:"derecha"}

# Creamos un control personalizado con esas teclas
mandos=pilas.control.Control(teclas)

# Definimos la clase de nuestro actor
class Hombre(pilasengine.actores.Actor):
    """Un actor que se mueve con las teclas a y s"""
    def iniciar(self):
        self.imagen=pilas.imagenes.cargar_grilla("andando.png",6)
# Hacemos que el actor se mueva con nuestro control personalizado
        self.aprender("MoverseConElTeclado",control=mandos)
        
chuck=Hombre(pilas)

pilas.ejecutar()