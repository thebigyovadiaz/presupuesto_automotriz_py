# -*- coding: utf-8 -*-
"""Funciones de uso común para tratamiento de fechas, lectura de
archivos e impresión de textos en pantalla.
"""

import datetime

def get_fecha_actual():
    """Retorna la fecha actual con formato dd/mm/aaaa"""
    hoy = datetime.datetime.now()
    fecha_actual = hoy.strftime("%d-%m-%Y")
    return fecha_actual


def sumar_dias(dias=0):
    """Suma N días a la fecha actual y la devuelve con formato
    dd/mm/aaaa. Argumentos:

    dias -- Cantidad de días a sumar a la fecha actual.

    """
    fecha = datetime.datetime.now() + datetime.timedelta(days=dias)
    nueva_fecha = fecha.strftime("%d-%m-%Y")
    return nueva_fecha


def leer_archivo(archivo):
    """Lee el contenido de un archivo y lo retorna como cadena de texto.
    Argumentos:

    archivo -- Ruta del archivo a ser leído
    """

    contenido = ""
    if archivo:
        filename = open(archivo, 'r')
        contenido = filename.read()
        filename.close()

    return contenido


def mostrar_texto(texto=""):
    """Imprime un texto determinado en pantalla.
    Argumentos:

    texto -- Texto a mostrar en pantalla.
    """

    if texto:
        print(texto)
