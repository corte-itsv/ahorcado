# Hangman / Ahorcado
"""Juego interactivo de ahorcado en español."""

from pathlib import Path
import random


ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
# Las letras acentuadas se adivinan con su letra base.
EQUIVALENCIAS = str.maketrans({
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u",
})


def normalizarLetra(letra):
    """Pasa una letra a minúscula y elimina los acentos relevantes."""
    return letra.lower().translate(EQUIVALENCIAS)


def elegirPalabra(listadoPalabras):
    """Devuelve una palabra elegida al azar de ``listadoPalabras``."""
    if not listadoPalabras:
        raise ValueError("El listado de palabras no puede estar vacío.")
    return random.choice(listadoPalabras)


def cargarPalabras():
    """Carga desde palabras.txt las palabras que pueden jugarse."""
    ruta = Path(__file__).with_name("palabras.txt")
    with ruta.open(encoding="utf-8") as archivo:
        palabras = [linea.strip().lower() for linea in archivo]

    # Se descartan entradas con espacios o signos: no se pueden adivinar letra a letra.
    return [palabra for palabra in palabras
            if palabra and all(normalizarLetra(letra) in ALFABETO for letra in palabra)]


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """Retorna True si todas las letras de la palabra ya fueron adivinadas."""
    letras = set(letrasMencionadas)
    return all(normalizarLetra(letra) in letras for letra in palabraSecreta)


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    """Muestra las letras acertadas y guiones bajos para las restantes."""
    letras = set(letrasMencionadas)
    return " ".join(
        letra if normalizarLetra(letra) in letras else "_"
        for letra in palabraSecreta
    )


def obtenLetrasDisponibles(letrasMencionadas):
    """Retorna las letras del alfabeto que todavía no se intentaron."""
    letras = set(letrasMencionadas)
    return "".join(letra for letra in ALFABETO if letra not in letras)


def obtenerLetra(letrasMencionadas):
    """Pide y valida una letra nueva, y la devuelve en minúscula."""
    while True:
        letra = normalizarLetra(input("Ingresá una letra: ").strip())

        if len(letra) != 1 or letra not in ALFABETO:
            print("Ingresá una única letra válida.")
        elif letra in letrasMencionadas:
            print("Ya ingresaste esa letra. Probá con otra.")
        else:
            return letra


def ahorcado(palabraSecreta):
    """Inicia una partida de ahorcado con ocho intentos incorrectos."""
    palabraSecreta = palabraSecreta.lower()
    letrasMencionadas = []
    intentosRestantes = 8

    print("¡Bienvenido al juego Ahorcado!")
    print(f"La palabra secreta tiene {len(palabraSecreta)} letras.")

    while intentosRestantes > 0 and not esPalabraAdivinada(
        palabraSecreta, letrasMencionadas
    ):
        print(f"\nTe quedan {intentosRestantes} intentos.")
        print("Letras disponibles:", obtenLetrasDisponibles(letrasMencionadas))
        print("Palabra:", obtenPalabraAdivinada(palabraSecreta, letrasMencionadas))

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        if letra in (normalizarLetra(caracter) for caracter in palabraSecreta):
            print("¡Bien! La letra está en la palabra.")
        else:
            intentosRestantes -= 1
            print("Esa letra no está en la palabra.")

    if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("\n¡Felicitaciones! Adivinaste la palabra:", palabraSecreta)
    else:
        print("\nSe terminaron los intentos. La palabra era:", palabraSecreta)


if __name__ == "__main__":
    listadoPalabras = cargarPalabras()
    palabraSecreta = elegirPalabra(listadoPalabras)
    ahorcado(palabraSecreta)
