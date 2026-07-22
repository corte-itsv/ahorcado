import random
import unicodedata
import os

def normalizar(letra):
    """
    Convierte á, é, í, ó, ú, ü en a, e, i, o, u.
    Mantiene la ñ.
    """
    if letra == "ñ":
        return "ñ"

    letra = unicodedata.normalize("NFD", letra)
    letra = "".join(c for c in letra if unicodedata.category(c) != "Mn")
    return letra.lower()


def elegirPalabra(listadoPalabras):
    return random.choice(listadoPalabras)


def cargarPalabras():
    with open("palabras.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido.split()


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    for letra in palabraSecreta:
        if normalizar(letra) not in letrasMencionadas:
            return False
    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    resultado = ""

    for letra in palabraSecreta:
        if normalizar(letra) in letrasMencionadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado.strip()


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
        letra = input("Ingresá una letra: ").lower()
        letra = normalizar(letra)

        if len(letra) != 1 or letra not in alfabeto:
            print("Ingresá una única letra válida.")
        elif letra in letrasMencionadas:
            print("Esa letra ya fue utilizada.")
        else:
            return letra


def ahorcado(palabraSecreta):
    intentos = 8
    letrasMencionadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    print("La palabra tiene", len(palabraSecreta), "letras.")

    while intentos > 0 and not esPalabraAdivinada(palabraSecreta, letrasMencionadas):

        print("\n--------------------------------")
        print("Intentos restantes:", intentos)
        print("Letras disponibles:", obtenLetrasDisponibles(letrasMencionadas))
        print("Palabra:", obtenPalabraAdivinada(palabraSecreta, letrasMencionadas))

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        encontrada = False

        for l in palabraSecreta:
            if normalizar(l) == letra:
                encontrada = True
                break

        if encontrada:
            print("¡Bien! La letra está en la palabra.")
        else:
            print("La letra no está en la palabra.")
            intentos -= 1

    print("\n==============================")

    if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("¡Felicitaciones! Adivinaste la palabra:", palabraSecreta)
    else:
        print("Perdiste.")
        print("La palabra era:", palabraSecreta)

listadoPalabras = cargarPalabras()
print(os.getcwd())
print(os.listdir())
palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)