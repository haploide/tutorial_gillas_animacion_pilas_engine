#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# andando05.py
# Andando y saltando usando grilla
#-----------------------------------------------------------------------
import pilasengine

pilas=pilasengine.iniciar()

VELOCIDAD=4

# Definimos las teclas que moveran al personaje
teclas = {pilas.simbolos.a:"izquierda", pilas.simbolos.s:"derecha", 
    pilas.simbolos.ESPACIO:"arriba"}

# Creamos un control personalizado con esas teclas
mandos=pilas.control.Control(teclas)

# Definimos la clase de nuestro actor
class Hombre(pilasengine.actores.Actor):
    """Un actor que se mueve con las teclas a, s y ESPACIO y con animación"""
    def iniciar(self):
        self.imagen=pilas.imagenes.cargar_grilla("andando.png",6)
        self.definir_cuadro(0)
        # Hacemos que el actor se mueva con nuestro control personalizado
        self.hacer_inmediatamente(Esperando)
    
    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)
    
class Esperando(pilasengine.comportamientos.Comportamiento):
    """Actor en posicion normal o esperando a que el usuario pulse alguna tecla"""
    def iniciar(self, receptor):
        self.receptor= receptor
        self.receptor.definir_cuadro(0)

    def actualizar(self):
        if mandos.izquierda:
            self.receptor.hacer_inmediatamente(Caminando)
        elif mandos.derecha:
            self.receptor.hacer_inmediatamente(Caminando)
        if mandos.arriba:
            self.receptor.hacer_inmediatamente(Saltando)
        
class Caminando(pilasengine.comportamientos.Comportamiento):
    """Actor caminando"""
    def iniciar(self, receptor):
        self.receptor = receptor
        self.cuadros = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
        self.paso = 0

    def actualizar(self):
        self.avanzar_animacion()
        
        if mandos.izquierda:
            if not self.receptor.espejado:
                self.receptor.espejado = True
            self.receptor.x-=VELOCIDAD
        elif mandos.derecha:
            if self.receptor.espejado:
                self.receptor.espejado = False
            self.receptor.x+=VELOCIDAD
        else:
           self.receptor.hacer_inmediatamente(Esperando)
        if mandos.arriba:
            self.receptor.hacer_inmediatamente(Saltando)
    
    def avanzar_animacion(self):
        self.paso +=1
        if self.paso >= len(self.cuadros):
            self.paso=0
        
        self.receptor.definir_cuadro(self.cuadros[self.paso])

class Saltando(pilasengine.comportamientos.Comportamiento):
    """Actor Saltando"""
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(0)
        self.origen = self.receptor.y
        self.dy = 10 
    def actualizar(self):
        self.receptor.y += self.dy
        self.dy -= 0.3
    
        if self.receptor.y < self.origen:
            self.receptor.y = self.origen
            self.receptor.hacer_inmediatamente(Esperando)
    
        if mandos.izquierda:
            self.receptor.x -= VELOCIDAD
        elif mandos.derecha:
            self.receptor.x += VELOCIDAD
                
            
        
chuck=Hombre(pilas)

pilas.ejecutar()