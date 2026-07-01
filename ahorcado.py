import random
import unicodedata


def normalizar(texto):
    """
    Convierte áéíóúü -> aeiouu
    Mantiene la ñ.
    """
    resultado = ""

    for letra in texto.lower():
        if letra == "ñ":
            resultado += "ñ"
        else:
            letra = unicodedata.normalize("NFD", letra)
            letra = "".join(c for c in letra if unicodedata.category(c) != "Mn")
            resultado += letra

    return resultado


def elegirPalabra(listadoPalabras):
    return random.choice(listadoPalabras)


def cargarPalabras():
    archivo = open("palabras.txt", "r", encoding="utf-8")
    palabras = []

    for linea in archivo:
        palabras.append(linea.strip())

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
            resultado += palabraSecreta[i] + " "
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

    while True:

        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:
            print("Debe ingresar una sola letra.")
            continue

        if letra not in "abcdefghijklmnñopqrstuvwxyz":
            print("Debe ingresar una letra válida.")
            continue

        if letra in letrasMencionadas:
            print("Ya ingresó esa letra.")
            continue

        return letra


def ahorcado(palabraSecreta):

    intentos = 8
    letrasMencionadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    print("La palabra tiene", len(palabraSecreta), "letras.")

    palabraNormalizada = normalizar(palabraSecreta)

    while intentos > 0:

        print("----------------------")
        print("Intentos restantes:", intentos)
        print("Letras disponibles:", obtenLetrasDisponibles(letrasMencionadas))
        print("Palabra:", obtenPalabraAdivinada(palabraSecreta, letrasMencionadas))

        letra = obtenerLetra(letrasMencionadas)

        letrasMencionadas.append(letra)

        if letra in palabraNormalizada:
            print("¡Correcto!")
        else:
            print("La letra no está en la palabra.")
            intentos -= 1

        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
            print()
            print("¡Felicitaciones!")
            print("La palabra era:", palabraSecreta)
            return

    print()
    print("Te quedaste sin intentos.")
    print("La palabra era:", palabraSecreta)


# --------------------------
# Programa principal

listadoPalabras = cargarPalabras()

palabraSecreta = elegirPalabra(listadoPalabras)

ahorcado(palabraSecreta)