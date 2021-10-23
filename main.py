# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:16:54 2021

@author: Emilio Porras
"""

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color
    
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
        
    def cantidadAsientos(self):
        count = 0
        for item in self.asientos:
            if item != None:
                count += 1
        return count
    
    def verificarIntegridad(self):
        registroMotor = self.motor.registro
        registroAuto = self.registro
        for item in self.asientos:
            if item != None:
                registroAsiento = item.registro
                if registroMotor == registroAuto and registroAuto == registroAsiento:
                    continue
                else:
                    return "Las piezas no son originales"
        return "Auto original"
    
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo
            