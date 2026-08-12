#   Hangman / Ahorcado

import random

# --- DIBUJOS DEL AHORCADO (Extra) ---
DIBUJOS_AHORCADO = [
    # 8 vidas (0 errores)
    """
       +---+
           |
           |
           |
           |
           |
    =========
    """,
    # 7 vidas (1 error)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # 6 vidas (2 errores)
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # 5 vidas (3 errores)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # 4 vidas (4 errores)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # 3 vidas (5 errores)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # 2 vidas (6 errores)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # 1 vida (7 errores)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    # 0 vidas (8 errores - Perdiste)
    """
       +---+
       |   |
      (X)  |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def quitar_tildes(texto):
    """
    Función auxiliar para normalizar los caracteres especiales.
    Convierte á->a, é->e, ü->u, etc.
    """
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    texto_normalizado = texto.lower()
    for original, reemplazo in reemplazos.items():
        texto_normalizado = texto_normalizado.replace(original, reemplazo)
    return texto_normalizado


def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)
    Devuelve una palabra elegida al azar del listado.
    """
    return random.choice(listadoPalabras)


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.
    """
    print("Cargando lista de palabras desde el archivo...")
    try:
        with open('palabras.txt', 'r', encoding='utf-8') as archivo:
            # Leemos todo el archivo y separamos por espacios/saltos de línea
            listado = archivo.read().split()
        print(f"¡Éxito! Se cargaron {len(listado)} palabras.")
        return listado
    except FileNotFoundError:
        print("Error: No se encontró 'palabras.txt'. Asegurate de que esté en la misma carpeta.")
        # Retorna una lista por defecto para que el programa no se rompa de la nada
        return ["python", "ahorcado", "programacion", "computadora"]


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: booleano, True si todas las letras de palabraSecreta están en letrasMencionadas
    '''
    palabra_norm = quitar_tildes(palabraSecreta)
    for letra in palabra_norm:
        if letra not in letrasMencionadas:
            return False
    return True


def obtenPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: string, con letras y guiones bajos que representan el estado parcial
    '''
    resultado = ""
    for letra in palabraSecreta:
        # Evaluamos la letra sin tilde para ver si el usuario la adivinó
        if quitar_tildes(letra) in letrasMencionadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()


def obtenLetrasDisponibles(letrasMencionadas):
    '''
    letrasMencionadas: list, letras ya intentadas
    retorna: string, con las letras (a..z + ñ) que aún NO se han intentado.
    '''
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    letras_restantes = ""
    for letra in abecedario:
        if letra not in letrasMencionadas:
            letras_restantes += letra
    return letras_restantes


def obtenerLetra(letrasMencionadas):
    """
    Pide al usuario ingresar una nueva letra.
    No distingue minúsculas de mayúsculas ni tildes.
    Valida que la letra no haya sido ingresada previamente sin descontar intentos.
    """
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    
    while True:
        ingreso = input("Ingresá una letra: ").lower()
        letra = quitar_tildes(ingreso) # Por si el usuario le clava una tilde al input
        
        if len(letra) != 1 or letra not in abecedario:
            print("❌ Por favor, ingresá una única letra válida (a-z o ñ).")
        elif letra in letrasMencionadas:
            print("⚠️ ¡Ya intentaste con esa letra! Probá con otra (no te descuento intentos).")
        else:
            return letra


def ahorcado(palabraSecreta):
    '''
    Inicia un juego interactivo de Ahorcado.
    '''
    vidas = 8
    letrasMencionadas = []
    palabra_norm = quitar_tildes(palabraSecreta) # Normalizamos la secreta para las comparaciones
    
    print("\n" + "="*40)
    print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
    print("="*40)
    print(f"Estoy pensando en una palabra que tiene {len(palabraSecreta)} letras.")
    
    # Bucle principal del juego
    while vidas > 0:
        print("\n" + "-"*40)
        print(DIBUJOS_AHORCADO[8 - vidas])
        print(f"Te quedan {vidas} intentos.")
        print(f"Letras disponibles: {obtenLetrasDisponibles(letrasMencionadas)}")
        print(f"Palabra: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")
        
        letra = obtenerLetra(letrasMencionadas)
        letrasMencionadas.append(letra)
        
        if letra in palabra_norm:
            print("\n✅ ¡Bien hecho! Esa letra está en mi palabra.")
        else:
            print("\n❌ ¡Oops! Esa letra no está en mi palabra.")
            vidas -= 1
            
        # Comprobamos si ya adivinó toda la palabra
        if esPalabraAdivinada(palabraSecreta, letrasMencionadas):
            print("\n" + "="*40)
            print("🎉 ¡FELICIDADES, GANASTE! 🎉")
            print(f"Adivinaste la palabra: '{palabraSecreta.upper()}'")
            print("="*40)
            break
            
    # Si sale del while y las vidas son 0, perdió
    if vidas == 0:
        print("\n" + "-"*40)
        print(DIBUJOS_AHORCADO[8])
        print("💀 ¡TE QUEDASTE SIN INTENTOS, PERDISTE! 💀")
        print(f"La palabra secreta era: '{palabraSecreta.upper()}'")
        print("="*40)


# --- EJECUCIÓN DEL JUEGO ---

# Cargamos la lista de palabras
listadoPalabras = cargarPalabras()

# Elegimos una y arrancamos el juego
palabraSecreta = elegirPalabra(listadoPalabras)
ahorcado(palabraSecreta)




