# -*- coding: utf-8 -*-
import webbrowser
from string import Template
from constantes import *
from helpers import leer_archivo, mostrar_texto

class ModeloDePresupuesto:
    # Datos comerciales
    titulo = "PRESUPUESTO"
    encabezado_nombre = "Autotruck Calabozo C.A"
    encabezado_web = "www.autotruckcalabozo.com.ve"
    encabezado_email = "info@autotruckcalabozo.com.ve"
    encabezado_direccion = "Calabozo - Edo. Guárico"
    fecha = FECHA_ACTUAL
    vencimiento = FECHA_CADUCIDAD

    # Datos impositivos
    alicuota_iva = 16

    # Propiedades relativas al formato
    html = TEMPLATE_HTML
    txt = TEMPLATE_TXT

    # Servicios y precios
    services = ('Motor', 'Caja', 'Tren', 'Frenos', 'Mantenimiento')
    motor = ['Servicio de ajustes y correción de fallas en el motor', 5000]
    caja = ['Servicio de ajustes y correción de fallas en la caja', 5000]
    tren = ['Servicio de ajustes y correción en el tren delantero/trasero', 4000]
    frenos = ['Servicio de ajustes y correción de fallas en los frenos', 4000]
    mantenimiento =['Servicio de camio de aceite y filtro', 3000]
    lista_precios = {'Motor': motor,
                     'Caja': caja,
                     'Tren': tren,
                     'Frenos': frenos,
                     'Mantenimiento': mantenimiento}

    # Setear los datos del cliente
    def set_cliente(self):
        self.cliente = input(NOMBRE_CLIENTE)
        self.rif = input(RIF)
        self.direccion = input(DIRECCION_CLIENTE)

    # Seleccionar tipo de plan
    def seleccionar_serv(self):
        texto_a_mostrar = ELEGIR_SERVICIO
        codigo_serv = 0

        for serv in self.services:
            texto_a_mostrar += '(%d)%s  ' % (codigo_serv, serv)
            codigo_serv += 1

        texto_a_mostrar += ": "
        elegir_serv = input(texto_a_mostrar)

        # Capturando excepciones
        try:
            elegir_serv = int(elegir_serv)
            self.serv = self.services[elegir_serv]
        except (ValueError, IndexError):
            mostrar_texto(DATO_INCORRECTO)
            self.seleccionar_serv()
        else:
            datos_servicio = self.lista_precios[self.services[elegir_serv]]
            self.servicio = datos_servicio[0]
            importe = datos_servicio[1]
            self.importe = float(importe)

    # Calcular IVA
    def calcular_iva(self):
        self.monto_iva = self.importe * self.alicuota_iva / 100

    # Calcula el monto total del presupuesto
    def calcular_neto(self):
        self.neto = self.importe + self.monto_iva

    # Armar numero de presupuesto
    def armar_numero_presupuesto(self):
        contador = open('contador.txt', 'r+')
        ultimo_num = int(contador.read())
        nuevo = ultimo_num + 1
        contador.seek(0)
        nuevo = str(nuevo)
        contador.write(nuevo)
        contador.close()
        self.numero_presupuesto = nuevo

    # Guardar presupuesto en archivo
    def guardar_presupuesto(self, txt, html):
        respuesta = input(GUARDAR_ARCHIVO)
        # Si el usuario indica "s"
        if respuesta.lower() == 'n':
            mostrar_texto(txt)
        # si en cambio el usuario indica "n"
        elif respuesta.lower() == 's':
            filename = 'presupuestos/'+self.numero_presupuesto+'.html'
            presupuesto = open(filename, 'w')
            presupuesto.write(html)
            presupuesto.close()
            mostrar_texto(CONFIRM_ARCHIVO_GUARDADO)
            self.mostrar_presupuesto(filename)
        # sino
        else:
            mostrar_texto(OPCION_INCORRECTA)
            self.guardar_presupuesto(txt, html)

    # Mostrar presupuesto en navegador
    def mostrar_presupuesto(self, archivo):
        respuesta = input(MOSTRAR_PRESUPUESTO)
        if respuesta.lower() == 's':
            webbrowser.open(BASE_DIR + "/" + archivo)

    # Armar el presupuesto
    def armar_presupuesto(self):
        """Esta función se encarga de armar todo el presupuesto"""
        self.armar_numero_presupuesto()
        txt = leer_archivo(self.txt)
        html = leer_archivo(self.html)

        # armo un diccionario con los datos del template
        diccionario = dict(nombre=self.encabezado_nombre,
                           web=self.encabezado_web,
                           ubicacion=self.encabezado_direccion,
                           email=self.encabezado_email,
                           titulo=self.titulo,
                           numero=self.numero_presupuesto,
                           fecha=self.fecha,
                           rif=self.rif,
                           cliente=self.cliente,
                           direccion=self.direccion,
                           serv=self.serv,
                           servicio=self.servicio,
                           precio=self.importe,
                           iva=self.monto_iva,
                           total=self.neto,
                           limite=self.vencimiento)

        txt = Template(txt).safe_substitute(diccionario)
        html = Template(html).safe_substitute(diccionario)
        self.guardar_presupuesto(txt, html)

    # Método constructor
    def __init__(self):
        mostrar_texto(ENCABEZADO_MODULO)
        self.set_cliente()
        self.seleccionar_serv()
        self.calcular_iva()
        self.calcular_neto()
        self.armar_presupuesto()

# Instanciar clase
presupuesto = ModeloDePresupuesto()
