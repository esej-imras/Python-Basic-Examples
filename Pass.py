#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from random import randint

lista1=[]

def passgen(n_min,n_may,digitos,passwd):
	"""
	Generacion de contraseñas aleatorias indicando el numero de argumentos junto con la cadena vacia como argumanto para conservar el valor de la variable y que pueda regresar el valor especificado en la contraseña para agregar cada una de las siguientes formas se utilizo ASCII
	
Generation of random passwords indicating the number of arguments along with the empty string as an argument to keep the value of the variable and that can return The value specified in the password to add each of the forms is used ASCII

	Rangos de ASCII / ASCII Range
	Numeros / Numbers	
	0-9 [48-57]
	Minusculas / Lowercase
	a-z [97-122]
	Mayusculas / Capital Letters
	A-Z [65-90]
	"""
	
	if digitos==0 and n_may==0 and n_min==0 :
		passwd=passwd.join(lista1)
		print passwd
	else:
		desc=randint(1,3)
		if desc==1 and n_min > 0:			
			lista1.append(chr(randint(97,122)))
			n_min-=1
			passwd=passgen(n_min,n_may,digitos,passwd)			
		elif desc==2 and n_may > 0:		
			lista1.append(chr(randint(65,90)))
			n_may-=1
			passwd=passgen(n_min,n_may,digitos,passwd)
		elif desc==3 and digitos > 0:		
			lista1.append(chr(randint(48,57)))
			digitos-=1
			passwd=passgen(n_min,n_may,digitos,passwd)
		else:
			passwd=passgen(n_min,n_may,digitos,passwd)
	return passwd

hola=passgen(2,3,4,'')
print hola
