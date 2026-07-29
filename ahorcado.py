import random

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
        texto=texto.replace(original, simple)
    return texto
def elegirPalabra(listadoPalabras):
    """
    listadoPalabras (list): lista de palabras (strings)

    Devuelve una palabra elegida al azar del listado.
    """
    #Sugerencia! ver: https://www.w3schools.com/python/module_random.asp


    pal_secret=random.choice(listadoPalabras)
    return pal_secret


def cargarPalabras():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas en minúsculas.

    Dependiendo del tamaño de la lista, esta función puede tardar un poco.
    """
    #Sugerencia! ver: https://www.w3schools.com/python/ref_func_open.asp
    list_palabras = open("palabras.txt", "r")
    palabras = list_palabras.read().split()
    list_palabras.close()
    return palabras


def esPalabraAdivinada(palabraSecreta, letrasMencionadas):
    '''
    palabraSecreta: string, la palabra que el usuario intenta adivinar
    letrasMencionadas: list, letras que ya fueron intentadas
    retorna: booleano, True si todas las letras de palabraSecreta están en letrasMencionadas;
             False en caso contrario
    '''
    for letra in palabraSecreta:
        if letra not in letrasMencionadas:
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

    estado = [letra if letra in letrasMencionadas else "_" for letra in palabraSecreta]
    return " ".join(estado)


def obtenLetrasDisponibles(letrasMencionadas):
    '''
    letrasMencionadas: list, letras ya intentadas
    retorna: string, con las letras (a..z) que aún NO se han intentado.
    '''
    # Sugerencia: empezá del alfabeto 'abcdefghijklmnopqrstuvwxyz' y remové las ya usadas.
    letras_disp = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(letrasMencionadas)):
        letras_disp = letras_disp.replace(letrasMencionadas[i], "")
    return letras_disp


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
        letra = input("Escribí una letra: ").lower()
        letra = normalizar(letra)
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresá una sola letra válida.")
        elif letra in letrasMencionadas:
            print("La letra ya fue ingresada, intentá con otra.")
        else:
            break
    letrasMencionadas.append(letra)
    return letra
    
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
    letrasMencionadas = []
    print(f"longitud de la palabra secreta: {len(palabraSecreta)}")
    intentos_rest=8
    while intentos_rest > 0:
        if esPalabraAdivinada(palabraSecreta, letrasMencionadas) == False:
                print(f"Progreso: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")
                letra = obtenerLetra(letrasMencionadas)
                if letra not in palabraSecreta:
                    intentos_rest -=1
                    print(f"La letra {letra} no esta en la palabra")
                else:
                    print(f"Bien, la letra {letra} esta en la palabra")
                    
                print(f"Letras disponibles: {obtenLetrasDisponibles(letrasMencionadas)}")
                print("-" * 25)
                print(f"intentos restantes: {intentos_rest}")
        else:
            print(f"Progreso: {obtenPalabraAdivinada(palabraSecreta, letrasMencionadas)}")
            print("Ganaste")
            break

    if intentos_rest <= 0:
        print(f"Perdiste, te quedaste sin intentos la palabra era {palabraSecreta}")


        


       
    





# Descomentar al completar las funciones:

# Cargamos la lista de palabras en la variable 'listadoPalabras'
# para que esté disponible en todo el programa

# Cuando termines tu función ahorcado, descomentá estas dos líneas para probar
# (pista: mientras probás, podés elegir vos la palabra secreta)

listadoPalabras = cargarPalabras()
palabraSecreta = normalizar(elegirPalabra(listadoPalabras))
ahorcado(palabraSecreta)