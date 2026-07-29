import random

def normalizar(letra):
    letra = letra.lower()
    letra = letra.replace("á", "a")
    letra = letra.replace("é", "e")
    letra = letra.replace("í", "i")
    letra = letra.replace("ó", "o")
    letra = letra.replace("ú", "u")
    letra = letra.replace("ü", "u")
    return letra


def elegirPalabra(listadoPalabras):
    return random.choice(listadoPalabras)


def cargarPalabras():
    archivo = open("palabras.txt", "r", encoding="utf-8")
    palabras = archivo.read().split()
    archivo.close()
    return palabras


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    for letra in palabraSecreta:
        if normalizar(letra) not in letrasMencionadas:
            return False
    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    palabra = ""

    for letra in palabraSecreta:
        if normalizar(letra) in letrasMencionadas:
            palabra = palabra + letra + " "
        else:
            palabra = palabra + "_ "

    return palabra


def obtenLetrasDisponibles(letrasMencionadas):
    alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v x y z"
    disponibles = ""

    for letra in alfabeto:
        if letra not in letrasMencionadas:
            disponibles = disponibles + letra

    return disponibles


def obtenerLetra(letrasMencionadas):
    while True:
        letra = input("Ingrese una posible letra: ").lower()

        if len(letra) != 1:
            print("Ingrese una letra unica.")
        elif letra not in "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z":
            print("Ingrese una letra válida.")
        elif letra in letrasMencionadas:
            print("Ya ingresó esa letra.")
        else:
            return letra


def ahorcado(palabraSecreta):

    intentos = 8
    letrasMencionadas = []

    print(f"¡Juguemos al ahorcado! \n")
    print("La palabra tiene", len(palabraSecreta), "letras.")

    while intentos > 0:

        print(f"___________________________ \n")
        if intentos == 8:
            print(" +--- \n | \n | \n | \n | \n | \n | \n ========= \n ")
        elif intentos == 7:
            print(" +---+ \n | \n | \n | \n | \n | \n | \n ========= \n ")
        elif intentos == 6:
            print(" +---+ \n |   O \n | \n | \n | \n | \n | \n ========= \n ")
        elif intentos == 5:
            print(" +---+ \n |   O \n |   I \n |   \n | \n | \n | \n ========= \n ")
        elif intentos == 4:
            print(" +---+ \n |   O \n |   I \n |   I\n | \n | \n | \n ========= \n ")
        elif intentos == 3:
            print(" +---+ \n |   O \n |  /I \n |   I\n | \n | \n | \n ========= \n ")
        elif intentos == 2: 
            print(" +---+ \n |   O \n |  /I\ \n |   I\n | \n | \n | \n ========= \n ")
        else:
            print(" +---+ \n |   O \n |  /I\ \n |   I\n |  /\n | \n | \n ========= \n ")
        
        print(f"___________________________ \n")
        print(f"Intentos que quedan: {intentos} \n")
        print(f"Letras disponibles: {obtenLetrasDisponibles(letrasMencionadas)} \n")
        print(f"Palabra a descubrir: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)} \n")

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        if letra in [normalizar(x) for x in palabraSecreta]:
            print("\nCorrecto.")
        else:
            print("\nIncorrecto.")
            intentos = intentos - 1

        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
            print()
            print("\n¡Lo lograste!")
            print("La palabra era:", palabraSecreta)
            return

    print()
    print("\nPerdiste.")
    print(" +---+ \n |   O \n |  /I\ \n |   I\n |  / \ \n | \n | \n ========= \n ")
    print("La palabra era:", palabraSecreta)


listadoPalabras = cargarPalabras()
palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)