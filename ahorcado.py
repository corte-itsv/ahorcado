import random

def normalizar_letra(letra):
    """
    Función  para convertir letras con tilde o diéresis
    a su caracter normal.
    """
    remplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    return remplazos.get(letra, letra)

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
    print("Cargando lista de palabras desde el archivo...")
    with open('palabras.txt', 'r', encoding='utf-8') as archivo:
        linea = archivo.read()
        listado = linea.lower().split()
    print(f"{len(listado)} palabras cargadas.")
    return listado
    

def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: booleano, True si todas las letras de palabraSecreta están en letrasMencionadas;
             False en caso contrario
    '''
    for letra in palabraSecreta:
        if normalizar_letra(letra) not in letrasMencionadas:
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
        if normalizar_letra(letra) in letrasMencionadas:
            resultado.append(letra)
        else:
            resultado.append('_')
    return ' '.join(resultado)



def obtenLetrasDisponibles(letrasMencionadas):
    '''
    letrasMencionadas: list, letras ya intentadas
    retorna: string, con las letras (a..z) que aún NO se han intentado.
    '''
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    disponibles = []
    for letra in alfabeto:
        if letra not in letrasMencionadas:
            disponibles.append(letra)
    return ''.join(disponibles)


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
        entrada = input("Ingresa una letra: ").strip().lower()

        if len(entrada) != 1 or entrada not in alfabeto:
            print("Por favor, ingresa una sola letra válida del abecedario.")
        elif entrada in letrasMencionadas:
            print("Ya habías ingresado esa letra. Intenta con otra.")
        else:
            return entrada


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
    ahorcado_dibujos = [
        """
           +---+
           |   |
          O    |
         /|\\   |
         / \\   |
               |
        =========""",
        """
           +---+
           |   |
          O    |
         /|\\   |
         /     |
               |
        =========""",
        """
           +---+
           |   |
          O    |
         /|\\   |
               |
               |
        =========""",
        """
           +---+
           |   |
          O    |
         /|    |
               |
               |
        =========""",
        """
           +---+
           |   |
          O    |
          |    |
               |
               |
        =========""",
        """
           +---+
           |   |
          O    |
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

    intentos = 8
    letrasMencionadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Estoy pensando en una palabra de {len(palabraSecreta)} letras.")

    palabra_normalizada = [normalizar_letra(c) for c in palabraSecreta]

    while intentos > 0 and not esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print("-" * 40)
        print(ahorcado_dibujos[intentos])
        print(f"Te quedan {intentos} intentos.")
        print(f"Letras disponibles: {obtenLetrasDisponibles(letrasMencionadas)}")

        letra_ingresada = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra_ingresada)

        if letra_ingresada in palabra_normalizada:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            print("Lo siento, esa letra no está en la palabra.")
            intentos -= 1

        print(f"Progreso: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")

    print("-" * 40)
    if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
        print(f"¡Felicidades, ganaste! La palabra era '{palabraSecreta}'.")
    else:
        print(ahorcado_dibujos[0])
        print(f"¡Te quedaste sin intentos! La palabra secreta era: {palabraSecreta}")

listadoPalabras = cargarPalabras()
palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)
