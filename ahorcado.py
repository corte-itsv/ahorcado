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
import unicodedata
def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    return random.choice(listadoPalabras)


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.

    Dependiendo del tamaño de la lista, esta función puede tardar un poco.
    """
    archivo = open("palabras.txt", "r", encoding="utf-8")
    palabras = archivo.read().split()
    archivo.close()
    return palabras

def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    palabra = normalizar(palabraSecreta)

    for letra in palabra:
        if letra not in letrasMencionadas:
            return False

    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    resultado = ""

    palabra = normalizar(palabraSecreta)

    for i in range(len(palabra)):
        if palabra[i] in letrasMencionadas:
            resultado += palabraSecreta[i]
        else:
            resultado += "_ "

    return resultado



def obtenLetrasDisponibles(letrasMencionadas):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    disponibles = ""

    for letra in alfabeto:
        if letra not in letrasMencionadas:
            disponibles += letra

    return disponibles


def obtenerLetra(letrasMencionadas):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    while True:
        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:
            print("Debe ingresar una sola letra.")
            continue

        if letra not in alfabeto:
            print("Letra inválida.")
            continue

        if letra in letrasMencionadas:
            print("Ya ingresaste esa letra.")
            continue

        return letra


def ahorcado(palabraSecreta):
    intentos = 8
    letrasMencionadas = []

    print("¡Bienvenido al Ahorcado!")
    print("La palabra tiene", len(palabraSecreta), "letras.")

    while intentos > 0:

        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
            print("¡Felicitaciones! Adivinaste la palabra:", palabraSecreta)
            return

        print("--------------------")
        print("Intentos restantes:", intentos)
        print("Letras disponibles:", obtenLetrasDisponibles(letrasMencionadas))
        print("Palabra:", obtenPalabraAdivinada(palabraSecreta, letrasMencionadas))

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        if letra in normalizar(palabraSecreta):
            print("¡La letra está en la palabra!")
        else:
            print("La letra no está.")
            intentos -= 1

    print("Perdiste.")
    print("La palabra era:", palabraSecreta)

    # Sugerencias:
    # - Usá un conjunto/lista para letrasMencionadas
    # - Llevá un contador de intentos restantes (inicialmente 8)
    # - En cada vuelta: mostrar letras disponibles, pedir input, validar que sea 1 letra a-z,
    #   manejar repetidos, actualizar estado, y chequear victoria/derrota.




# Descomentar al completar las funciones:

# Cargamos la lista de palabras en la variable 'listadoPalabras'
# para que esté disponible en todo el programa

listadoPalabras = cargarPalabras()

# Cuando termines tu función ahorcado, descomentá estas dos líneas para probar
# (pista: mientras probás, podés elegir vos la palabra secreta)

palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)




