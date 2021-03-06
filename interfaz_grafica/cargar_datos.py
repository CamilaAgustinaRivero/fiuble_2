# Daniel, Gonzalez
"""
Función: cargar_datos_usuarios()
Parámetros:
    no tiene
Salidas:
    obtiene la información de los usuarios ya registrados y la pasa a un diccionario
"""


def cargar_datos_usuarios():
    datos_usuarios = open("datos_usuarios.csv", "r")
    linea = datos_usuarios.readline()
    usuario, clave = linea.rstrip("\n").split(",") if linea else ('', '')
    dict_datos = {}

    while linea:
        dict_datos[usuario] = clave
        linea = datos_usuarios.readline()
        usuario, clave = linea.rstrip("\n").split(",") if linea else ('', '')
    datos_usuarios.close()
    return dict_datos
