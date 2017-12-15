#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
"""
    Trabajando con POO Python
    
"""
from poo1 import Becario
from random import choice

lista=[]
calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        becarioobjeto=Becario(b,choice(calificaciones))
        lista.append(becarioobjeto)
    return lista

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

a=asigna_calificaciones()
imprime_calificaciones()

print a
