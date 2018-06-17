#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# andando03.py
# Movimiento simple manual con uso de grilla
#-----------------------------------------------------------------------
import pilasengine

pilas=pilasengine.iniciar()

# Definimos las teclas que moveran al personaje
teclas = {pilas.simbolos.a:"izquierda", pilas.simbolos.s:"derecha"}

# Creamos un control personalizado con esas teclas
mandos=pilas.control.Control(teclas)

# Definimos la clase de nuestro actor
class Hombre(pilasengine.actores.Actor):
    """Un actor que se mueve con las teclas a y s y con animación"""
    def iniciar(self):
        self.imagen=pilas.imagenes.cargar_grilla("andando.png",6)
        self.cuadro=0
        # Hacemos que el actor se mueva con nuestro control personalizado
        self.aprender("MoverseConElTeclado",control=mandos)
    
    def actualizar(self):
        # Miramos si se han pulsado las teclas adecudas para cambiar, en
        # su caso, la imagen de la grilla y hacia donde mira
        if mandos.izquierda:
            if not self.espejado:
                self.espejado = True
            self.cuadro+=1
        elif mandos.derecha:
            if self.espejado:
                self.espejado = False
            self.cuadro+=1
        else:
            self.cuadro=0
        if self.cuadro>5:
            self.cuadro=1
            
        self.imagen.definir_cuadro(self.cuadro)
                
            
        
chuck=Hombre(pilas)

pilas.ejecutar()