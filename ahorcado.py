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

# Abecedario completo incluyendo la 'ñ'
LETRAS_VALIDAS = "abcdefghijklmnñopqrstuvwxyz"


def normalizarCaracter(caracter):
    """
    Función auxiliar para remover acentos y diéresis manteniendo la 'ñ' y 'Ñ'.
    Ejemplo: 'á' -> 'a', 'Ü' -> 'u', 'Ñ' -> 'ñ'.
    """
    caracter = caracter.lower()
    if caracter == 'ñ':
        return 'ñ'
    forma_nfd = unicodedata.normalize('NFD', caracter)
    sin_tilde = "".join(c for c in forma_nfd if unicodedata.category(c) != 'Mn')
    return sin_tilde


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    if not listadoPalabras:
        return ""
    return random.choice(listadoPalabras).lower()


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.

    Dependiendo del tamaño de la lista, esta función puede tardar un poco.
    """
    print("Cargando lista de palabras desde el archivo...")
    try:
        with open("palabras.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            listado = contenido.split()
            print(f"  {len(listado)} palabras cargadas.")
            return listado
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'palabras.txt'.")
        return []


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: booleano, True si todas las letras de palabraSecreta están en letrasMencionadas;
             False en caso contrario
    '''
    for letra in palabraSecreta:
        letra_norm = normalizarCaracter(letra)
        if letra_norm not in letrasMencionadas:
            return False
    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: string, con letras y guiones bajos que representan
             el estado parcial de la palabra adivinada hasta ahora.
             Ej.: 'a_ _ le' para 'apple' si solo se adivinó 'a' y 'l' y 'e'.
    '''
    resultado = []
    for letra in palabraSecreta:
        letra_norm = normalizarCaracter(letra)
        if letra_norm in letrasMencionadas:
            resultado.append(letra)
        else:
            resultado.append("_")
    return " ".join(resultado)


def obtenLetrasDisponibles(letrasMencionadas):
    '''
    letrasMencionadas: list, letras ya intentadas
    retorna: string, con las letras (a..z) que aún NO se han intentado.
    '''
    disponibles = []
    for letra in LETRAS_VALIDAS:
        if letra not in letrasMencionadas:
            disponibles.append(letra)
    return "".join(disponibles)


def obtenerLetra(letrasMencionadas):
    """
    Pide al usuario ingresar una nueva letra.
    No distingue minúsculas de mayúsculas.
    Valida que la letra no haya sido ingresada previamente.
    letras válidas: abcdefghijklmnñopqrstuvwxyz

    letrasMencionadas: list, letras ya intentadas
    retorna: string nueva letra ingresada por el usuario, en minúsculas
    """
    while True:
        entrada = input("Por favor, ingresa una letra: ").strip()
        
        if len(entrada) != 1:
            print("Entrada no válida. Debes ingresar una ÚNICA letra.")
            continue
            
        letra = normalizarCaracter(entrada)
        
        if letra not in LETRAS_VALIDAS:
            print("Carácter no válido. Usa letras del abecedario (incluyendo 'ñ').")
            continue
            
        if letra in letrasMencionadas:
            print(f"Ya habías intentado la letra '{letra}'. ¡Intenta con otra!")
            continue
            
        return letra


def dibujarAhorcado(intentos):
    """
    Función auxiliar opcional para dibujar el ahorcado según los intentos restantes.
    """
    etapas = [
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
               |
               |
               |
               |
               |
        =========""",
        """
               |
               |
               |
               |
               |
        ========="""
    ]
    return etapas[intentos]


def ahorcado(palabraSecreta):
    '''
    palabraSecreta: string, la palabra secreta a adivinar.

    Inicia un juego interactivo de Ahorcado.
    '''
    intentos = 8
    letrasMencionadas = []

    print("Bienvenido al juego Ahorcado!")
    print(f"Estoy pensando en una palabra que tiene {len(palabraSecreta)} letras.")

    while intentos > 0 and not esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("------------------------------------------")
        print(dibujarAhorcado(intentos))
        print(f"Te quedan {intentos} intentos.")
        print(f"Letras disponibles: {obtenLetrasDisponibles(letrasMencionadas)}")
        
        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)

        # Normalizamos la palabra secreta para verificar si la letra está presente
        palabra_normalizada = [normalizarCaracter(c) for c in palabraSecreta]

        if letra in palabra_normalizada:
            print(f"¡Buena jugada! La letra '{letra}' está en la palabra: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")
        else:
            intentos -= 1
            print(f"¡Lástima! La letra '{letra}' no está en la palabra: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")

    print("------------------------------------------")
    if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("¡Felicitaciones, ganaste!")
    else:
        print(dibujarAhorcado(0))
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabraSecreta}'.")


# Bloque de ejecución principal
if __name__ == "__main__":
    listadoPalabras = cargarPalabras()
    if listadoPalabras:
        palabraSecreta = elegirPalabra(listadoPalabras)
        ahorcado(palabraSecreta)
    # Sugerencias:
    # - Usá un conjunto/lista para letrasMencionadas
    # - Llevá un contador de intentos restantes (inicialmente 8)
    # - En cada vuelta: mostrar letras disponibles, pedir input, validar que sea 1 letra a-z,
    #   manejar repetidos, actualizar estado, y chequear victoria/derrota.




# Descomentar al completar las funciones:

# Cargamos la lista de palabras en la variable 'listadoPalabras'
# para que esté disponible en todo el programa

# listadoPalabras = cargarPalabras()

# Cuando termines tu función ahorcado, descomentá estas dos líneas para probar
# (pista: mientras probás, podés elegir vos la palabra secreta)

# palabraSecreta = elegirPalabra(listadoPalabras)
# ahorcado(palabraSecreta)
