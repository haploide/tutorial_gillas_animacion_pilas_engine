#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# andando01.py
# Movimiento Automático
#-----------------------------------------------------------------------
import pilasengine

pilas=pilasengine.iniciar()

# Definimos la clase de nuestro actor
class Hombre(pilasengine.actores.Actor):
    """Un actor que se mueve con el teclado"""
    def iniciar(self):
        self.imagen=pilas.imagenes.cargar_grilla("andando.png",6)
        self.aprender("MoverseConElTeclado")
        
chuck=Hombre(pilas)

pilas.ejecutar()