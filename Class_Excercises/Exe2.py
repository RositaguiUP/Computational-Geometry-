
from Functions_Library import *
from random import randint, seed

# Exercise 2
# https://colab.research.google.com/drive/1Ki-GhkYXz_5did6Kg8YQT_jV8KtsEXZq?authuser=1

# 1 Rotar el punto  (10,3)  90 grados antihorario con respecto al origen. Imprime las nuevas coordenadas.
a = Point(10, 3)
a.rotate(90)
print(f"Point (10, 3) rotate 90° is {a}")

# 2 Rotar el mismo punto  (10,3)  77 grados antihorario alrededor del origen. Imprime las nuevas coordenadas
a = Point(10, 3)
a.rotate(77)
print(f"Point (10, 3) rotate 77° is {a}")

# 3 Calcula la distancia euclidiana entre los puntos  (2,2)  y  (6,5) . Agrega la función de distancia euclidiana a la clase punto.
a = Point(2, 2)
b = Point(6, 5)
print(f"Distance (2,2) and (6,5) is {a}")

# 4 Ordenamiento
seed(50771708)
points= [Point(randint(-100,100), randint(-100,100)) for i in range(30)]
print(f"\nList of points:\n{points}")

# Para el conjunto de puntos dado, ordena los puntos por su  x  en orden ascendente, en caso de empate, ordena por su  y  en orden ascendente.
points.sort(key=lambda p: (p.x, p.y))
print(f"\nList of points 2:\n{points}")

# Para el conjunto de puntos dado, ordena los puntos por su  y  en orden descendente, en caso de empate, ordena por su  x  en orden descendente.
points.sort(key=lambda p: (-p.y, -p.x))
print(f"\nList of points 3:\n{points}")

# Para el conjunto de puntos dado, ordena los puntos con respecto a su ángulo, iniciando en la horizontal, en sentido antihorario
points.sort(key=lambda p: p.angle)
print(f"\nList of points 4:\n{points}")