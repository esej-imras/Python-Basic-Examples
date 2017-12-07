#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
"""	
Funcion modificada para que sin importar como se encuentren los elementos del arreglo sean convertidos a mayusculas y puedan ser correctamente comparados elemento.upper() --> Contenido en mayuscula, en general la funcion busca los becarios no aprobados.

Modified function so that no matter how they are the elements of the arrangement are converted to upper case and can be correctly compared item.upper () -> Content in capital letters, in general the function looks for the non-approved scholars.
"""
    nombre_completo = nombre_completo.upper()
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['GERARDO', 'ALAN', 'GUADALUPE', 'RAFAEL', 'KARINA']:
            return False
    aprobados.append(nombre_completo)
    return True

def inserta_becario(nombre_completo):
"""
Funcion que inserta un becario con la funcion append que lo agrega al final de la lista, posteriormente lo ordena con la funcion sort() para que la lista quede por orden alfabetico.

Function that inserts a grantee with the append function that adds it to the end of the list, then orders it with the sort () function so that the list is in alphabetical order. 
"""
	becarios.append(nombre_completo)
	becarios.sort()
	print becarios
	
def borra_becario (new_bec,becarios):
"""
Funcion que borra un becario ingresado de la lista de becarios la cual pasa como argumento, busca el elemento si, lo encuentra lo borra y devuelve true, si no devuelve False.

Function that deletes a scholar entered from the list of fellows which passes as an argument, looks for the element if, finds it deletes it and returns true, if it does not return False.
"""	
	num_arr=0
	for c in becarios:
		if c==new_bec :
			becarios.pop(num_arr)
			return True	
		else:
			num_arr+=1
	return False

becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez Gerardo',
            'Diez Gutierrez Gonzalez Rafael'
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia Fernanda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline Karina',
            'Palacio Nieto Esteban',
            'Reyes Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']

for b in becarios:
    if aprueba_becario(b):
        print 'APROBADO: ' + b
    else:
        print 'REPROBADO: ' + b

new_bec='Ramos Tagle Jesus'
inserta_becario(new_bec)
if borra_becario(new_bec,becarios):
	print 'Se borro el registro del becario'
else:
	print 'Error no se encontro el becario'

print becarios
