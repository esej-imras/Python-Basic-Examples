#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']

print (lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias)
print filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias))
print map (lambda nombre: nombre.upper(),filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias)))
print '\n\n\n'
print (lambda x: ','.join(x))(map (lambda nombre: nombre.upper(),filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias))))
#print map (lambda nombre: nombre.upper(),(lambda w,x,y,z: w+x+y+z)#(sistemas,op_interna,incidentes,auditorias))

"""
Programacion funcional:
	Funcion lambda que sume las listas sistemas,op_interna,incidentes,auditorias
	Busca los nombres con i en la lista resultante del primer ejemplo
	Convierte a mayusculas el resultado anterior
"""
