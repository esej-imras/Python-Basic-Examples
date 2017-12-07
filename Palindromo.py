#!usr/bin/python
# -*- coding: utf-8 -*-
# UNAM-CERT

def palindrome():
	"""
Funcion que lee desde terminal una palabra y determina si es un palindromo
comparando que la cadena original sea igual a la cadena inversa que se obtiene con un slice a la lista.

Function that reads from terminal a word and determines if it is a palindrome
comparing that the original string is equal to the reverse string obtained with a slice to the list.
	"""
	b=raw_input()
	c=b[::-1]
	if b==c:
		print "TRUE"
		return True			
	else:
		print "FALSE"
		return False

print "Ingrese el Palindromo:\n"
palindrome()
