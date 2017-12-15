#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sarmiento Campos José
# Sarmiento Campos Maria Guadalupe
#UNAM-CERT
#XML - parser

import sys
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime

hosts=[]
extra=[]

class Host:
	"""
		Clase que define los elementos de interes de host
		Class that defines the elements of host interest
	"""
	def __init__(self,ip,estado,puertos):
		self.ip = ip
		self.estado = estado
		self.puertos = puertos
	def __str__(self):
		return 'IP %s\nEstado %s\nPuertos Abiertos \n%s\n' % (self.ip,self.estado,self.puertos)


def printError(msg, exit = False):
	"""
		Imprime el mensaje de error
		Print err msg
	"""
	sys.stderr.write('Error:\t%s\n' % msg)
	if exit:
	sys.exit(1)

def hashes(archivo_nmap):
	"""
		Obtiene el valor de los hash del archivo que se desee mediante llamadas al sistema
		Get the value of the hashes of the desired file by calling the system
	"""
	p = subprocess.Popen(["md5sum",archivo_nmap],stdout=subprocess.PIPE)
	res1 = p.communicate()[0]
	md51 = ''
	for element in res1:
		if element==' ':
			break
		else:
			md51+=element 
	p = subprocess.Popen(["sha1sum",archivo_nmap],stdout=subprocess.PIPE)
	res = p.communicate()[0]
	sha11 = ''
	for element in res:
		if element==' ':
			break
		else:
			sha11+=element
	return md51,sha11

def lee_xml(archivo_nmap):
	"""
		Lee el archivo xml y lo convierte en una lista con todos los elementos de interes para el usuario final
		Read the xml file and convert it into a list with all the elements of interest for the end user
	"""
    with open(archivo_nmap,'r') as nmap:
    	root = ET.fromstring(nmap.read())
    	for hoster in root.findall('.//host'):
		state = hoster.find('status').get('state')
		ip = hoster.find('address').get('addr')	    
	    	ports = hoster.findall('.//port')
		puertos=''
		for i in range(len(ports)):
			port = ports[i].get('portid')
			sta = ports[i].find('state').get('state')
	    		http = ports[i].find('service').get('name')
			puertos=puertos+port+':'+sta+':'+http+'\n' 
         	host = Host(ip,state,puertos)
         	hosts.append(host)

def F2L(archivo):
	"""
		Convierte archivos en listas manipulables
		Convert files to manipulable lists
	"""
	listatmp=[]
	with open(archivo,'r') as Archivo_Interno:
		for linea in Archivo_Interno.readlines():
			listatmp.append(linea[:-1])
	return listatmp	

def escribe_intermedio(archivo_reporte,a,b):
	"""
		Escribe el archivo intermedio que sirve para generar el reporte final
		Write the intermediate file used to generate the final report
	"""
	with open('inter.txt','w') as intermedio:
	map(lambda u: output.write(str(u)),hosts)        
	intermedio.close()
	escribe_reporte(archivo_reporte)

def escribe_reporte(archivo):
	"""
		Con ayuda de un reporte intermedio genera el reporte final contando cada uno de los elementos de interes en nmap.xml
		With the help of an intermediate report generates the final report counting each of the elements of interest in nmap.xml
	"""
	with open(archivo_reporte,'w') as output:
        output.write(str(datetime.now()) + '\n')
	output.write(str(a) + '\n')
	output.write(str(b) + '\n')
	extra=F2L('inter.txt')
	apache=len(filter(lambda a: 'http' in a,extra))
	honey=len(filter(lambda a: 'honeypot' in a,extra))
	p80=len(filter(lambda a: '80:open' in a,extra))
	p22=len(filter(lambda a: '22:open' in a,extra))
	p53=len(filter(lambda a: '53:open' in a,extra))
	p443=len(filter(lambda a: '443:open' in a,extra))
	up=len(filter(lambda a: 'up' in a,extra))
	down=len(filter(lambda a: 'down' in a,extra))
	output.write('Host up:'+ str(up) + '\n')
	output.write('Host down:'+ str(down) + '\n')
	output.write('Port 22:'+ str(p22) + '\n')
	output.write('Port 53:'+ str(p53) + '\n')
	output.write('Port 80:'+ str(p80) + '\n')
	output.write('Port 443:'+ str(p443) + '\n')
	output.write('Host Apache:'+ str(apache) + '\n')
	output.write('Host Honey:'+ str(honey) + '\n')	

if __name__ == '__main__':
	"""
		Recibe los argumentos para indicar el reporte detallado
		Receive the arguments to indicate the detailed report
	"""
    if len(sys.argv) != 3:
        printError('Indicar archivo a leer y archivo de reporte.', True)
    else:
	md52,sha12=hashes(sys.argv[1])        
	lee_xml(sys.argv[1])
        escribe_reporte(sys.argv[2],md52,sha12)
