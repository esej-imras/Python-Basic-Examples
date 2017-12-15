#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
"""
		Expresiones regulares en python la primera busca octetos validos en una ip
		La segunda valida correos electronicos
"""
ipex=r'((([2][5][0-5]|[2][0-4][0-9]|[0-1][0-9][0-9])+\.){3}([2][5][0-5]|[2][0-4][0-9]|[0-1][0-9][0-9])+)'
correo=r'[A-Za-z0-9]+@[a-z]+\.[a-z]+'