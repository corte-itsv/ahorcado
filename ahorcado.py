

import random


ALFABETO = "abcdefghijklmnñopqrstuvwxyz"


def normalizarTexto(texto):
    """
    Convierte el texto a minúsculas y reemplaza las vocales acentuadas
    por sus letras base. La letra ñ se mantiene.
    """
    reemplazos = str.maketrans({
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u"
    })

    return texto.lower().translate(reemplazos)


def elegirPalabra(listadoPalabras):
    """
    Devuelve una palabra elegida al azar del listado.
    """
    return random.choice(listadoPalabras)


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas obtenidas de palabras.txt.
    """
    with open("palabras.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    palabras = contenido.split()
    listadoPalabras = []

    for palabra in palabras:
        listadoPalabras.append(palabra.lower())

    return listadoPalabras


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """
    Retorna True si todas las letras de la palabra fueron adivinadas.
    Retorna False en caso contrario.
    """
    for letra in palabraSecreta:
        letraNormalizada = normalizarTexto(letra)

        if letraNormalizada not in letrasMencionadas:
            return False

    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """
    Retorna la palabra mostrando las letras descubiertas y guiones bajos
    para las letras que todavía no fueron adivinadas.
    """
    palabraMostrada = ""

    for letra in palabraSecreta:
        letraNormalizada = normalizarTexto(letra)

        if letraNormalizada in letrasMencionadas:
            palabraMostrada += letra + " "
        else:
            palabraMostrada += "_ "

    return palabraMostrada.strip()


def obtenLetrasDisponibles(letrasMencionadas):
    """
    Retorna las letras que todavía no fueron utilizadas.
    """
    letrasDisponibles = ""

    for letra in ALFABETO:
        if letra not in letrasMencionadas:
            letrasDisponibles += letra

    return letrasDisponibles


def obtenerLetra(letrasMencionadas):
    """
    Pide al usuario una única letra válida que no haya sido utilizada.
    """
    while True:
        letraIngresada = input("Ingresá una letra: ").strip()
        letraIngresada = normalizarTexto(letraIngresada)

        if len(letraIngresada) != 1:
            print("Debés ingresar una única letra.")

        elif letraIngresada not in ALFABETO:
            print("El carácter ingresado no es una letra válida.")

        elif letraIngresada in letrasMencionadas:
            print("Esa letra ya fue utilizada. Ingresá otra.")

        else:
            return letraIngresada


def dibujarAhorcado(intentosRestantes):
    """
    Muestra el dibujo del ahorcado de acuerdo con la cantidad de
    intentos perdidos.
    """
    dibujos = [
        """
          +-------+
          |       |
                  |
                  |
                  |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
                  |
                  |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
          |       |
                  |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
         /|       |
                  |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
         /|\\      |
                  |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
         /|\\      |
          |       |
                  |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
         /|\\      |
          |       |
         /        |
        ===========
        """,
        """
          +-------+
          |       |
          O       |
         /|\\      |
          |       |
         / \\      |
        ===========
        """,
        """
          +-------+
          |       |
         [O]      |
         /|\\      |
          |       |
         / \\      |
        ===========
        """
    ]

    errores = 8 - intentosRestantes
    print(dibujos[errores])


def ahorcado(palabraSecreta):
    """
    Inicia un juego interactivo de Ahorcado.
    """
    intentosRestantes = 8
    letrasMencionadas = []

    print("======================================")
    print("          JUEGO DEL AHORCADO")
    print("======================================")
    print(
        "La palabra secreta tiene",
        len(palabraSecreta),
        "letras."
    )
    print("Tenés 8 intentos para descubrirla.")

    dibujarAhorcado(intentosRestantes)

    print(
        "Palabra:",
        obtenPalabraAdivinada(
            palabraSecreta,
            letrasMencionadas
        )
    )

    print(
        "Letras disponibles:",
        obtenLetrasDisponibles(letrasMencionadas)
    )

    print("Intentos restantes:", intentosRestantes)

    while (
        intentosRestantes > 0
        and not esPalabraAdivinada(
            palabraSecreta,
            letrasMencionadas
        )
    ):
        print("--------------------------------------")

        letraIngresada = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letraIngresada)

        palabraNormalizada = normalizarTexto(palabraSecreta)

        if letraIngresada in palabraNormalizada:
            print(
                "¡Correcto! La letra",
                letraIngresada,
                "pertenece a la palabra."
            )
        else:
            print(
                "La letra",
                letraIngresada,
                "no pertenece a la palabra."
            )

            intentosRestantes -= 1

        dibujarAhorcado(intentosRestantes)

        print(
            "Palabra:",
            obtenPalabraAdivinada(
                palabraSecreta,
                letrasMencionadas
            )
        )

        print(
            "Letras disponibles:",
            obtenLetrasDisponibles(letrasMencionadas)
        )

        print("Intentos restantes:", intentosRestantes)

    print("======================================")

    if esPalabraAdivinada(
        palabraSecreta,
        letrasMencionadas
    ):
        print("¡Felicitaciones! Adivinaste la palabra.")
        print("La palabra era:", palabraSecreta)
    else:
        print("Te quedaste sin intentos.")
        print("La palabra secreta era:", palabraSecreta)

    print("======================================")


if __name__ == "__main__":
    listadoPalabras = cargarPalabras()
    palabraSecreta = elegirPalabra(listadoPalabras)
    ahorcado(palabraSecreta)