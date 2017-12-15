#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
"""
	Trabajando con diccionarios que tienen los numeros odiosos menores a 50
"""
diccionario={i:(bin(i),hex(i)) for i in range(51) if bin(i).count('1')%2!=0}
print dicccionario