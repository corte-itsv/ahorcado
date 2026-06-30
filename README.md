# Trabajo Práctico — Ahorcado

## Objetivo

El objetivo de esta actividad es implementar una versión del clásico juego **Ahorcado** utilizando Python, aplicando los conceptos vistos en la materia:

* Funciones
* Condicionales (`if`, `elif`, `else`)
* Bucles (`for`, `while`)
* Listas y cadenas de caracteres
* Modularización del código
* Entrada y salida por consola
* Validación de datos

---

## Archivos del ejercicio

La actividad se encuentra en el archivo:

```text
ahorcado.py
```

Además, se utilizará un archivo con las palabras disponibles:

```text
palabras.txt
```

Ambos archivos deben permanecer en el mismo directorio.

---

## Consigna

Deberás completar las funciones indicadas en `ahorcado.py` para implementar un juego interactivo de Ahorcado entre el usuario y la computadora.

La computadora deberá seleccionar una palabra al azar del archivo `palabras.txt` y el jugador intentará descubrirla letra por letra.

---

## Requisitos

El programa deberá cumplir con las siguientes condiciones:

* La palabra secreta debe elegirse aleatoriamente del archivo `palabras.txt`.
* Al comenzar el juego se debe indicar cuántas letras tiene la palabra.
* En cada turno el usuario debe ingresar **una única letra**.
* Después de cada intento se debe informar inmediatamente si la letra pertenece o no a la palabra.
* Luego de cada ronda se debe mostrar:

  * El estado actual de la palabra (utilizando `_` para las letras no descubiertas).
  * Las letras que todavía no fueron utilizadas.
  * La cantidad de intentos restantes.

---

## Reglas del juego

* El jugador dispone de **8 intentos**.
* Solo se pierde un intento cuando la letra ingresada **no pertenece** a la palabra.
* Si el usuario repite una letra:

  * Se debe informar que ya fue utilizada.
  * **No** debe descontarse un intento.
* El juego finaliza cuando:

  * El jugador descubre toda la palabra, o
  * Se queda sin intentos.
* Si el jugador pierde, el programa debe revelar la palabra secreta.

---

## Consideraciones

El programa debe cumplir además con las siguientes condiciones:

* Las letras válidas son:

```text
abcdefghijklmnñopqrstuvwxyz
```

* No debe diferenciar entre mayúsculas y minúsculas.

Por ejemplo:

```text
A == a
Ñ == ñ
```

* Las vocales acentuadas y otros caracteres equivalentes deben considerarse como su letra base.

Ejemplos:

```text
á -> a
é -> e
í -> i
ó -> o
ú -> u
ü -> u
```

Es decir, si la palabra contiene una **á** y el usuario ingresa **a**, la letra debe considerarse correcta.

---

## Funciones a implementar

Se deberán completar las siguientes funciones:

* `elegirPalabra()`
* `cargarPalabras()`
* `esPalabraAdivinada()`
* `obtenPalabraAdivinada()`
* `obtenLetrasDisponibles()`
* `obtenerLetra()`
* `ahorcado()`

Cada función deberá respetar la documentación y los parámetros indicados en el archivo entregado.

---

## Extra (opcional)

Como mejora del juego, se puede reemplazar o complementar el contador de intentos restantes con el dibujo tradicional del ahorcado, actualizándolo cada vez que el usuario pierde una vida.

---

## Recomendaciones

* Resolver primero las funciones auxiliares antes de implementar `ahorcado()`.
* Probar cada función por separado antes de integrarla.

---

## Modalidad de trabajo

La resolución del ejercicio deberá realizarse utilizando **Git** y **GitHub**.

### 1. Crear una rama personal

Antes de comenzar a programar, cada alumno deberá crear una rama a partir de `main`.

La rama deberá tener el siguiente formato:

```text
apellido_nombre
```

Por ejemplo:

```text
perez_juan
gomez_maria
```

### 2. Resolver el ejercicio

Implementar las funciones solicitadas directamente en el archivo `ahorcado.py`.

### 3. Realizar commits

Se recomienda realizar commits pequeños y con mensajes descriptivos.

Ejemplos:

```text
Implementa funciones auxiliares
Completa lógica del juego
Corrige validación de letras
```

### 4. Crear un Pull Request

Una vez finalizado el ejercicio, cada alumno deberá crear un **Pull Request (PR)** desde su rama personal hacia la rama `main`.

La entrega será evaluada tanto por el funcionamiento del programa como por el correcto uso de Git y GitHub.
