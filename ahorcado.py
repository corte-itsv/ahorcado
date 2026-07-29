import random

alfabeto = "abcdefghijklmnñopqrstuvwxyz"


def quitarAcentos(texto):
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u"
    }

    resultado = ""
    for letra in texto:
        resultado += reemplazos.get(letra, letra)

    return resultado


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    palabra_elegida = random.choice(listadoPalabras)
    return palabra_elegida


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.
    """
    with open("palabras.txt", "r", encoding="utf-8") as archivo:
        return archivo.read().split()


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    """
    for letra in palabraSecreta:
        if quitarAcentos(letra) not in letrasMencionadas:
            return False
    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """
    Devuelve la palabra con las letras adivinadas y "_" en las restantes.
    """
    palabra_guiones = ""

    for letra in palabraSecreta:
        if quitarAcentos(letra) in letrasMencionadas:
            palabra_guiones += f" {letra} "
        else:
            palabra_guiones += " _ "

    return palabra_guiones


def obtenLetrasDisponibles(letrasMencionadas):
    """
    Devuelve las letras que todavía no fueron usadas.
    """
    letras_sin_intentar = ""

    for letra in alfabeto:
        if letra not in letrasMencionadas:
            letras_sin_intentar += letra

    return letras_sin_intentar


def obtenerLetra(letrasMencionadas):
    """
    Pide al usuario ingresar una letra válida.
    """
    letras_validas = list(alfabeto)

    while True:
        letra_user = input("Ingresa una letra: ").lower()

        if len(letra_user) != 1:
            print("Tiene que ingresar solo una letra.")
        elif letra_user not in letras_validas:
            print("No es una letra válida.")
        elif letra_user in letrasMencionadas:
            print("Letra ya ingresada.")
        else:
            return letra_user


def ahorcado(palabraSecreta):
    """
    Inicia el juego del ahorcado.
    """
    INTENTOS = 8
    letras_mencionadas = []

    print("================== AHORCADO ==================")
    print(f"\nLa palabra secreta tiene {len(palabraSecreta)} letras.")
    print(f"Palabra: {obtenPalabraAdivinada(palabraSecreta, letras_mencionadas)}")

    while INTENTOS > 0:
        print(f"\nIntentos restantes: {INTENTOS}")
        print(f"Letras disponibles: {obtenLetrasDisponibles(letras_mencionadas)}")

        letra_user = obtenerLetra(letras_mencionadas)
        letras_mencionadas.append(letra_user)

        veces_letra = 0

        for letra in palabraSecreta:
            if quitarAcentos(letra) == letra_user:
                veces_letra += 1

        if veces_letra > 0:
            print("La letra está dentro de la palabra.")
        else:
            print("La letra no está dentro de la palabra.")
            INTENTOS -= 1

        print(f"Estado: {obtenPalabraAdivinada(palabraSecreta, letras_mencionadas)}")
        print("==============================================")

        if esPalabraAdivinada(palabraSecreta, letras_mencionadas):
            print("¡Adivinaste!")
            print(f"La palabra era: {palabraSecreta}")
            return

    print("Perdiste.")
    print(f"La palabra era: {palabraSecreta}")


listadoPalabras = cargarPalabras()
palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)