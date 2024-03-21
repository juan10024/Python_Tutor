# Chrome Cat - Juego con Pygame

Este proyecto es un juego de corredor infinito desarrollado en Python utilizando la biblioteca Pygame. El juego presenta un gato como personaje principal que debe correr por un camino lleno de obstáculos, como cactus y pájaros, mientras intenta evitar colisiones. Muchas gracias al área de Recursos Humanos de __Plataforma en línea para habilidades digitales - Kodland__ por proponer un reto tan interesante.

kodland.org

![Logo del proyecto](https://github.com/juan10024/Python_Tutor/blob/31637480b74d232d7acb7e7aed8ccb663c77ff3e/Screenshot_2.png)

## Funcionalidades

- **Control del Gato**: El jugador puede controlar al gato utilizando las teclas de flecha hacia arriba y hacia abajo para saltar y agacharse respectivamente.
  
- **Generación de Obstáculos**: Se generan aleatoriamente obstáculos a lo largo del camino que el jugador debe esquivar.
  
- **Puntuación**: El juego registra la puntuación del jugador en función de la distancia recorrida y el tiempo que sobrevive.
  
- **Menú de Selección**: Al iniciar el juego, se presenta un menú donde el jugador puede seleccionar entre diferentes mapas y niveles de dificultad.
  
- **Pantalla de Game Over**: Si el jugador colisiona con un obstáculo, se muestra una pantalla de Game Over con la puntuación final y la opción de reiniciar el juego.

__Generalidades del código__

Aquí hay una seccuencia básica del flujo del programa:

Importa las clases y funciones necesarias:
```python
import pygame
import os
import random
```

Inicializa Pygame y configura la pantalla:
```python
pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

Crea instancias del jugador y otros objetos del juego:
```python
player = Cat()
cloud = Cloud()
```

Ejecuta el bucle principal del juego:
```python
while True:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
exit()
```

## Contenido del Repositorio

El repositorio contiene los siguientes archivos y directorios principales:

- **`main.py`**: Este archivo contiene el código principal del juego, incluyendo la lógica del juego, la creación de instancias de personajes y obstáculos, y la interacción con el usuario.

- **`Assets`**: Este directorio contiene las imágenes utilizadas en el juego, como los sprites del gato, los obstáculos, el fondo y otros elementos visuales.

- **`README.md`**: Este archivo es la documentación del proyecto, proporcionando información sobre el juego, su funcionalidad y cómo ejecutarlo.

## Requisitos del Sistema

Para ejecutar el juego, se requiere tener instalado Python 3 y la biblioteca Pygame. Puedes instalar Pygame utilizando "pip install pygame"

