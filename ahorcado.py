#   Hangman / Ahorcado
#
#
#   En este problema vas a programar una variación del clásico juego Ahorcado. Si no
#   conoces las reglas, podes leer sobre ellas fácilmente. En nuestro caso, el segundo
#   jugador siempre será la computadora, que elegirá una palabra al azar.
#
#   Vas a implementar una función llamada ahorcado (hangman en inglés) que inicia y
#   lleva adelante un juego interactivo de Ahorcado entre un jugador y la computadora.
#   Antes de llegar a esa función, implementaremos algunas funciones auxiliares para
#   ponerte en marcha.
#
#   Para este ejercicio necesitas los archivos ps3_ahorcado.py y palabras.txt, los cuales
#   podes descargar desde el classroom. Asegúrate de guardarlos en el mismo directorio
#   donde vas a trabajar.
#
#   Requisitos:
#       • La computadora debe seleccionar al azar una palabra de la lista cargada
#         desde palabras.txt.
#       • El juego debe ser interactivo y fluir así:
#           - Al comenzar, indica al usuario cuántas letras tiene la palabra.
#           - Pide una única letra por ronda.
#           - Inmediatamente después de cada intento, informa si la letra está o no
#             en la palabra.
#           - Tras cada ronda, muestra el avance parcial (con guiones bajos en las
#             letras no descubiertas) y las letras no usadas aún.
#       • Reglas adicionales:
#           - El usuario dispone de 8 intentos. Recuérdale cuántos le quedan
#             después de cada ronda.
#           - Solo se pierde un intento cuando la letra no está en la palabra.
#           - Si el usuario repite una letra, no le quites un intento; en su lugar,
#             avísale y pídele otra.
#           - El juego termina cuando el usuario adivina toda la palabra o se queda
#             sin intentos. Si pierde, revela la palabra al final.
#       • Consideraciones:
#           - Las letras disponibles deben ser: 'abcdefghijklmnñopqrstuvwxyz'
#           - El programa no debe diferenciar entre minúsculas y mayúsculas, es decir,
#             es lo mismo si el usuario ingresa 'U' o 'u'
#           - Los caracetes especiales en las palabras en juego, como: á é í ó ú ü, deben
#             ser consideradas como correctas cuando el usuario ingresa su caracter base,
#             es decir, si hay una 'ü' en la palabra a adivinar, y el usuario ingresa 'u',
#             debe considerarse como correcto.
#       • Extra:
#           - En lugar, o en complemento, de mostrar la cantidad de vidas restantes, dibujá
#             el típico ahorcado a medida que el usuario vaya perdiendo vidas.
#


import random

def cargarPalabras():
    lista_final = []

    listadoPalabras = open("palabras.txt", "r", encoding="utf-8")

    for palabra in listadoPalabras:
        palabra_nueva = palabra.strip()
        if palabra_nueva != "":
            lista_final.append(palabra_nueva)

    listadoPalabras.close()

    return lista_final


def elegirPalabra(listadoPalabras):
    palabra_elegida = random.choice(listadoPalabras)
    return palabra_elegida


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):

    for letra in palabraSecreta:

        if letra == "á":
            comprobar = "a"
        elif letra == "é":
            comprobar = "e"
        elif letra == "í":
            comprobar = "i"
        elif letra == "ó":
            comprobar = "o"
        elif letra == "ú" or letra == "ü":
            comprobar = "u"
        else:
            comprobar = letra

        if comprobar not in letrasMencionadas:
            return False

    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):

    palabra = ""

    for letra in palabraSecreta:

        if letra == "á":
            comprobar = "a"
        elif letra == "é":
            comprobar = "e"
        elif letra == "í":
            comprobar = "i"
        elif letra == "ó":
            comprobar = "o"
        elif letra == "ú" or letra == "ü":
            comprobar = "u"
        else:
            comprobar = letra

        if comprobar in letrasMencionadas:
            palabra = palabra + letra + " "
        else:
            palabra = palabra + "_ "

    return palabra



def obtenLetrasDisponibles(letrasMencionadas):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    disponibles = ""

    for letra in alfabeto:
        if letra not in letrasMencionadas:
            disponibles = disponibles + letra

    return disponibles


def obtenerLetra(letrasMencionadas):
    while True:

        letra = input("Ingrese una letra: ")
        letra = letra.lower()

        if len(letra) != 1:
            print("Debe ingresar una sola letra.")
            continue

        if letra not in "abcdefghijklmnñopqrstuvwxyz":
            print("Debe ingresar una letra válida.")
            continue

        if letra in letrasMencionadas:
            print("Ya ingresaste esa letra.")
            continue

        return letra

def dibujarAhorcado(intentos):

    if intentos == 8:
        print("""
             +---+
             |   |
                 |
                 |
                 |
                 |
            =========
            """)

    elif intentos == 7:
        print("""
             +---+
             |   |
             O   |
                 |
                 |
                 |
            =========
            """)

    elif intentos == 6:
        print("""
             +---+
             |   |
             O   |
             |   |
                 |
                 |
            =========
            """)

    elif intentos == 5:
        print("""
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
            =========
            """)
        
    elif intentos == 4:
        print("""
             +---+
             |   |
             O   |
            /|\\  |
                 |
                 |
            =========
            """)

    elif intentos == 3:
        print("""
             +---+
             |   |
             O   |
            /|\\  |
            /    |
                 |
            =========
            """)

    elif intentos == 2:
        print("""
             +---+
             |   |
             O   |
            /|\\  |
            / \\  |
                 |
            =========
            """)

    elif intentos == 1:
        print("""
             +---+
             |   |
            [O   |
            /|\\  |
            / \\  |
                 |
            =========
            """)

    elif intentos == 0:
        print("""
             +---+
             |   |
            [O]  |
            /|\\  |
            / \\  |
                 |
            =========
            """)
    else:
        return

def ahorcado(palabraSecreta):

    letrasMencionadas = []
    intentos = 8

    tamaño_de_palabra = len(palabraSecreta)
    print("¡Bienvenido al Ahorcado!")
    print(f"La palabra tiene {tamaño_de_palabra} letras.")

    while True:
        print("--------------------------------")
        dibujarAhorcado(intentos)
        print(f"Intentos restantes: {intentos}")

        letras_disponibles = obtenLetrasDisponibles(letrasMencionadas)
        print(f"Letras disponibles: {letras_disponibles}")
        palabra = obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)
        print(f"Palabra: {palabra}")

        letra = obtenerLetra(letrasMencionadas)

        letrasMencionadas.append(letra)

        encontrada = False

        for caracter in palabraSecreta:

            if caracter == letra:
                encontrada = True

            elif caracter == "á" and letra == "a":
                encontrada = True

            elif caracter == "é" and letra == "e":
                encontrada = True

            elif caracter == "í" and letra == "i":
                encontrada = True

            elif caracter == "ó" and letra == "o":
                encontrada = True

            elif (caracter == "ú" or caracter == "ü") and letra == "u":
                encontrada = True

        if encontrada:
            print("¡Bien! La letra está en la palabra.")
        else:
            print("La letra no está en la palabra.")
            intentos = intentos - 1

        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):

            print("--------------------------------")
            print("¡Felicitaciones!")
            print("Adivinaste la palabra:", palabraSecreta)
            break

        if intentos == 0:
            dibujarAhorcado(intentos)
            print("--------------------------------")
            print("Te quedaste sin intentos.")
            print("La palabra era:", palabraSecreta)
            break




# Descomentar al completar las funciones:

# Cargamos la lista de palabras en la variable 'listadoPalabras'
# para que esté disponible en todo el programa
listadoPalabras = cargarPalabras()


palabra_elegida = elegirPalabra(listadoPalabras)
# Cuando termines tu función ahorcado, descomentá estas dos líneas para probar
# (pista: mientras probás, podés elegir vos la palabra secreta)

palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)