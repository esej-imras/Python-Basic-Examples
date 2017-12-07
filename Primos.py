#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

listaprimos=[]
b=int(raw_input())

def es_primo(numero):
	"""
Busca el numero primo en un rango desde 2 hasta (numero-1), si cualquiera de los elementos al dividirlo da un reciduo de cero, quiere decir que es divisible y por lo tanto no es primo, ademas de tener la restriccion de uno ya que no es primo.

Find the prime number in a range from 2 to (number-1), if any of the elements when dividing gives a recurrence of zero, it means that it is divisible and therefore it is not prime, in addition to having the restriction of one already which is not a prime number
	"""
	for i in range(2, numero):
		if numero<2:
			return False
		if numero % i == 0: 
			return False
	return True


def busca_primos(numero_de_primos,cont_asc):
	"""
	Recibes un número de numeros primos (limite de numeros a mostrar) y un contador ascendente para lograr el valor de cada uno de los numeros primos que compruebas con la funcion anterior y ponerlos en una lista que la función retornara al final.

	You receive a number of prime numbers (limit of numbers to show) and an ascending counter to get the value of each of the prime numbers you check with the previous function and put them in a list that the function will return at the end.
	"""
	if numero_de_primos==0:
		return listaprimos
	else:
		if es_primo(cont_asc):
			listaprimos.append(cont_asc)
			#print cont_asc
			#print numero_de_primos
			numero_de_primos-=1
			cont_asc+=1
			busca_primos(numero_de_primos,cont_asc)
		else:
			cont_asc+=1
			busca_primos(numero_de_primos,cont_asc) 
		
es_primo(b)
busca_primos(b,2,listaprimos)
