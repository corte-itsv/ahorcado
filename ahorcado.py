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


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    #Sugerencia! ver: https://www.w3schools.com/python/module_random.asp
    return random.choice(listadoPalabras)


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.

    Dependiendo del tamaño de la lista, esta función puede tardar un poco.
    """
    #Sugerencia! ver: https://www.w3schools.com/python/ref_func_open.asp
    file = open('palabras.txt', 'r')


    palabras = []

    for palabra in file:
        palabras.append(palabra[:-1])

    file.close()
    return palabras


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: booleano, True si todas las letras de palabraSecreta están en letrasMencionadas;
             False en caso contrario
    '''
    for letter in normalizar(palabraSecreta):
        if letter not in letrasMencionadas:
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
    # Sugerencia: construí un string acumulando letra o '_' según corresponda.
    palabra = '    '
    norm = normalizar(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if norm[i] in letrasMencionadas:
            palabra += palabraSecreta[i]
        else:
            palabra += '_'

    return palabra



def obtenLetrasDisponibles(letrasMencionadas):
    '''
    letrasMencionadas: list, letras ya intentadas
    retorna: string, con las letras (a..z) que aún NO se han intentado.
    '''
    # Sugerencia: empezá del alfabeto 'abcdefghijklmnopqrstuvwxyz' y remové las ya usadas.
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

    for letter in letrasMencionadas:
        alfabeto = alfabeto.replace(letter,'')

    return alfabeto


def normalizar(texto):
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
    }
    for original, simple in reemplazos.items():
        texto = texto.replace(original, simple)
    return texto


def obtenerLetra(letrasMencionadas):
    """
    Pide al usuario ingresar una nueva letra.
    No distingue minúsculas de mayúsculas.
    Valida que la letra no haya sido ingresada previamente.
    letras válidas: abcdefghijklmnñopqrstuvwxyz

    letrasMencionadas: list, letras ya intentadas
    retorna: string nueva letra ingresada por el usuario, en minúsculas
    """
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    while True:
        letra = ''
        letra = input('Ingrese una letra: ')

        if len(letra) != 1:
            print('Debe ingresar solo 1 (UNA) letra\n')
            continue

        if not letra.lower() in alfabeto:
            print('Eso no es una letra!\n')
            continue

        if letra.lower() in letrasMencionadas:
            print('Ya has ingresado esa letra!\n')
            continue
        else:
            return letra.lower()


def ahorcado(palabraSecreta):
    '''
    palabraSecreta: string, la palabra secreta a adivinar.

    Inicia un juego interactivo de Ahorcado.

    * Al inicio, informá cuántas letras tiene palabraSecreta.

    * Pedí al usuario una sola letra por ronda.

    * Informá inmediatamente si su letra aparece o no en la palabra.

    * Tras cada ronda, mostrale el estado parcial de la palabra,
      y también las letras que aún no ha usado.

    Seguí las demás limitaciones descriptas en el enunciado (8 intentos, no
    descontar por letras repetidas, terminar al adivinar toda la palabra o al
    quedarse sin intentos; si pierde, mostrar la palabra).
    '''
    # Sugerencias:
    # - Usá un conjunto/lista para letrasMencionadas
    # - Llevá un contador de intentos restantes (inicialmente 8)
    # - En cada vuelta: mostrar letras disponibles, pedir input, validar que sea 1 letra a-z,
    #   manejar repetidos, actualizar estado, y chequear victoria/derrota.
    HANGMANPICS = [
    '''
       ---+
          |
          |
          |
          |
          |
    =========''',
    '''
      +---+
          |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''']

    intentos = 8
    letrasMencionadas = []

    print('¡Bienvenido/a al juego, Ahorcado!')
    print(f'Estoy pensando en una palabra de {len(palabraSecreta)} letras.')

    while True:
        print(HANGMANPICS[8 - intentos], '\n')
        print(obtenPalabraAdivinada(palabraSecreta, letrasMencionadas), '\n')
        print(obtenLetrasDisponibles(letrasMencionadas), '\n')

        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)
        if not letra in normalizar(palabraSecreta):
            intentos -= 1

        if intentos == 0:
            print(HANGMANPICS[8], f'\nLo lamento, ya no tienes oportunidades. La palabra era {palabraSecreta}.')
            break

        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
            print(HANGMANPICS[8 - intentos], '\n', f'\nHas descubierto la palabra sectreta: {palabraSecreta}!')
            break





# Descomentar al completar las funciones:

# Cargamos la lista de palabras en la variable 'listadoPalabras'
# para que esté disponible en todo el programa

listadoPalabras = cargarPalabras()

# Cuando termines tu función ahorcado, descomentá estas dos líneas para probar
# (pista: mientras probás, podés elegir vos la palabra secreta)

palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)




