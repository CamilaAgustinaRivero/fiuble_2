from tkinter import messagebox
from cargar_datos import cargar_datos_usuarios
import sys

sys.path.append("..")
from main import main

# Daniel, Gonzalez
"""
Función: validar_clave()
Parámetros:
    clave: clave introducida por el usuario
Salidas:
    Devuelve True o False luego de validar la clave
"""


def validar_clave(clave):
    letras_con_acentos = ["á", "é", "í", "ó", "ú"]
    tiene_acento = tiene_mayus = tiene_minus = tiene_num = caracter_especial = caracter_dif = False
    for caracter in clave:
        if caracter in letras_con_acentos:
            tiene_acento = True
        elif caracter.islower():
            tiene_minus = True
        elif caracter.isupper():
            tiene_mayus = True
        elif caracter.isdigit():
            tiene_num = True
        elif caracter in ["_", "-"]:
            caracter_especial = True
        else:
            caracter_dif = True
    clave_valida = 8 <= len(
        clave) <= 15 and tiene_num and tiene_mayus and tiene_minus and not tiene_acento and caracter_especial and not caracter_dif
    return clave_valida


# Daniel, Gonzalez
"""
Función: validar_usuario()
Parámetros:
    usuario: Nombre de usuario ingresado
Salidas:
    Devuelve True o False dependiendo de la validación hecha sobre el nombre de usuario ingresado
"""


def validar_usuario(usuario):
    caracteres_alpha = [caracter.isalpha() for caracter in usuario]
    caracteres_num = [caracter.isdigit() for caracter in usuario]
    caracter_invalido = False
    for caracter in usuario:
        if caracter.isalpha() or caracter.isdigit() or caracter == "_":
            continue
        else:
            print(caracter, "invalido")
            caracter_invalido = True
    usuario_valido = 4 <= len(usuario) <= 15 and any(caracteres_alpha) and any(caracteres_num) and (
            "_" in usuario) and not caracter_invalido
    return usuario_valido


# Daniel, Gonzalez
"""
Función: verificar_ingreso_clave()
Parámetros:
    usuario_1: Primer nombre de usuario ingresado
    clave_1: Clave asociada al primer usuario ingresado
    modo_juego: '1' para modo un jugador o '2' para modo 2 jugadores
    raiz_main: raiz de main_interfaz
    raiz_login: raiz de ventana_login
    usuario_2: Segundo nombre de usuario ingresado o '' por defecto
    clave_2: Clave asociada al segundo nombre de usuario ingresado
Salidas:
"""


def verificar_ingreso_clave(usuario1, clave1, modo_juego, raiz_main, raiz_login, usuario2='', clave2=''):
    claves = cargar_datos_usuarios()
    if modo_juego == 1:
        if usuario1 in claves.keys():
            if claves[usuario1] == clave1:
                messagebox.showinfo(title=None, message="Usuario y Clave Correctos (correr main fiuble)")
                raiz_main.destroy();
                raiz_login.destroy()
                main(str(modo_juego), usuario1)
            else:
                messagebox.showerror(title=None, message="Algunos de los datos ingresados es Incorrecto")
        else:
            messagebox.showerror(title=None, message="Usuario no registrado")
    else:
        if usuario1 and usuario2 in claves.keys():
            if claves[usuario1] == clave1 and claves[usuario2] == clave2:
                messagebox.showinfo(title=None, message="Usuarios y Claves Correctos (correr main fiuble)")
                raiz_main.destroy();
                raiz_login.destroy()
                main(str(modo_juego), usuario1, usuario2)
            else:
                messagebox.showerror(title=None,
                                     message="Algunos de los datos ingresados es Incorrecto (clave incorrecta)")
        else:
            messagebox.showerror(title=None, message="Alguno de los usuarios no se encuentra registrado")
