# -*- coding: utf-8 -*-
"""Constantes predefinidas"""

import os
from helpers import get_fecha_actual, sumar_dias

# Constantes para métodos de entrada
RIF = "\tRIF: "
NOMBRE_CLIENTE = "\tNombre del cliente: "
DIRECCION_CLIENTE = "\tDirección: "
GUARDAR_ARCHIVO = "\n\t¿Desea guardar el presupuesto? (s/n): "
ELEGIR_SERVICIO = "\tServicio ofrecido "
MOSTRAR_PRESUPUESTO = "\t¿Desea ver el presupuesto generado? (s/n): "

# Fechas
DIAS_VALIDEZ = 5  # Días de validez del presupuesto
FECHA_ACTUAL = get_fecha_actual()
FECHA_CADUCIDAD = sumar_dias(DIAS_VALIDEZ)

# Rutas
BASE_DIR = os.getcwd()
TEMPLATES_DIR = "templates/"
TEMPLATE_HTML = TEMPLATES_DIR + "template.html"
TEMPLATE_TXT = TEMPLATES_DIR + "template.txt"

# Textos de las vistas
DIVLINE = "=" * 80
ENCABEZADO_MODULO = DIVLINE + "\n\tGENERACIÓN DEL PRESUPUESTO\n" + DIVLINE
CONFIRM_ARCHIVO_GUARDADO = "\n\tEl archivo se ha guardado exitosamente!\n\n"
OPCION_INCORRECTA = "\n\tOpción incorrecta. No se guardó el presupuesto.\n\n"
DATO_INCORRECTO = ("\n\tERROR: Tipo de dato incorrecto u opción fuera \
						de rango\n")
