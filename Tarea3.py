#!/usr/bin/python
# -*- coding: utf-8 -*-
#SARMIENTO CAMPOS JOSÉ, SARMIENTO CAMPOS MARÍA GUADALUPE
#UNAM-CERT 

def generador_contrasenas(archivo1, archivo2):
	"""
	La siguiente función lee un archivo linea por linea y transforma la frase leída en una contraseña, posteriormente crea un artchivo txt 
	donde se guardaran las contraseñas creadas
	"""
	with open(archivo1,'r') as frase, open(archivo2,'w') as password:
		for linea in frase.readlines():
			letralist=[]		
			for letra in linea:
				if letra==' ':
					letralist.append('_')
				else:
					for i in range(65,91):
						if letra=='A':#4
							letralist.append('4')
							break
						elif letra=='O':#0
							letralist.append('0')
							break
						elif letra=='E':#3
							letralist.append('3')
							break
						elif letra=='L':#1
							letralist.append('1')
							break
						elif letra=='I':#1
							letralist.append('1')
							break
						elif letra=='B':#6
							letralist.append('6')
							break
						elif chr(i)==letra:
							letralist.append(letra.lower())
							break
					
					for i in range(97,123):
						if letra=='a':#4
							letralist.append('4')
							break
						elif letra=='o':#0
							letralist.append('0')
							break
						elif letra=='e':#3
							letralist.append('3')
							break
						elif letra=='l':#1
							letralist.append('1')
							break
						elif letra=='i':#1
							letralist.append('1')
							break
						elif letra=='b':#6
							letralist.append('6')
							break
						elif chr(i)==letra:
							letralist.append(letra.upper())
							break
					if letra=='0':
						letralist.append('O')
					elif letra=='1':
						letralist.append('l')
					elif letra=='2':
						letralist.append('dos')
					elif letra=='3':
						letralist.append('E')
					elif letra=='4':
						letralist.append('A')
					elif letra=='5':
						letralist.append('cInCo')
					elif letra=='6':
						letralist.append('SeIs')
					elif letra=='7':
						letralist.append('SiEtE')
					elif letra=='8':
						letralist.append('OcHo')
					elif letra=='9':
						letralist.append('NuEvE')
						
			print(''.join(letralist))
			password.write(''.join(letralist)+'\n')
						

generador_contrasenas('password.txt', 'password_new.txt')
