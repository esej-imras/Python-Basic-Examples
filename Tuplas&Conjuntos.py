#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
"""
    Manejo de tuplas y conjuntos
"""
from random import choice
list1=[]
list2=[]
note_bec = {}
con=set()
notes = (0,1,2,3,4,5,6,7,8,9,10)
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
        note_bec[b] = choice(notes)

def imprime_calificaciones():
    for alumno in note_bec:
        print '%s obtuvo la calificacion %s\n' % (alumno,note_bec[alumno])

def reprobados():
    for alumno in note_bec:
        if note_bec[alumno]>=8:
            #aprobados
            list1.append(alumno)
        else:
            #reprobados
            list2.append(alumno)
    tupla2=tuple(list2)
    tupla1=tuple(list1)
    return tupla1,tupla2

def prom():
    n=0
    for alumno in note_bec:
        n+=note_bec[alumno]
    promedio=n/(len(note_bec))
    return promedio        

def conjuntocal():
    for alumno in note_bec:
        conj.add(note_bec[alumno])
    return conj        

asigna_calificaciones()
imprime_calificaciones()
tup,tup2=reprobados()
promedio=prom()
con=conjuntocal()
print "Aprobados "+ str(tup) 
print "Reprobados "+str(tup2)
print "Promedio : " + str(promedio)
print con
