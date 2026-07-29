import random


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    return random.choice(listadoPalabras)


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas.
    """
    archivo = open("palabras.txt", "r", encoding="utf-8")
    palabras = archivo.read().split()
    archivo.close()
    return palabras


def normalizar(letra):
    letra = letra.lower()

    if letra == "á":
        return "a"
    elif letra == "é":
        return "e"
    elif letra == "í":
        return "i"
    elif letra == "ó":
        return "o"
    elif letra == "ú" or letra == "ü":
        return "u"

    return letra


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: True si todas las letras fueron adivinadas.
    '''

    for letra in palabraSecreta:
        if normalizar(letra) not in letrasMencionadas:
            return False

    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    Devuelve la palabra mostrando solo las letras adivinadas.
    '''

    resultado = ""

    for letra in palabraSecreta:
        if normalizar(letra) in letrasMencionadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado


def obtenLetrasDisponibles(letrasMencionadas):
    '''
    Devuelve las letras que aún no fueron usadas.
    '''

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    disponibles = ""

    for letra in alfabeto:
        if letra not in letrasMencionadas:
            disponibles += letra

    return disponibles


def obtenerLetra(letrasMencionadas):
    """
    Pide una letra válida al usuario.
    """

    while True:

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1:
            print("Debes ingresar una sola letra.")
            continue

        if letra not in "abcdefghijklmnñopqrstuvwxyz":
            print("Letra inválida.")
            continue

        if letra in letrasMencionadas:
            print("Ya ingresaste esa letra.")
            continue

        return letra


def ahorcado(palabraSecreta):
    '''
    Inicia el juego de ahorcado.
    '''

    intentos = 8
    letrasMencionadas = []

    print("¡Bienvenido al Ahorcado!")
    print("La palabra tiene", len(palabraSecreta), "letras.")

    while intentos > 0 and not esPalabraAdivinada(palabraSecreta, letrasMencionadas):

        print("-----------------------------------")
        print("Intentos restantes:", intentos)
        print("Letras disponibles:", obtenLetrasDisponibles(letrasMencionadas))
        print("Palabra:", obtenPalabraAdivinada(palabraSecreta, letrasMencionadas))

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        encontro = False

        for caracter in palabraSecreta:
            if normalizar(caracter) == letra:
                encontro = True
                break

        if encontro:
            print("¡Bien! La letra está en la palabra.")
        else:
            print("La letra no está en la palabra.")
            intentos -= 1

    print("-----------------------------------")

    if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("¡Felicitaciones! Adivinaste la palabra:", palabraSecreta)
    else:
        print("Perdiste.")
        print("La palabra era:", palabraSecreta)


# Cargamos la lista de palabras
listadoPalabras = cargarPalabras()

# Elegimos una palabra al azar
palabraSecreta = elegirPalabra(listadoPalabras)

# Iniciamos el juego
ahorcado(palabraSecreta)