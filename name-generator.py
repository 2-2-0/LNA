# name generator exercise
# algorithmic narrative lab / (LNA in spanish)
# Variable random mixing from lists (made for soldiers in a RTS)
# by 220 & AA (2019) GPLv3 license

import random

lista_nombres = ["Alfredo", "Alejandro", "Armando", "Román", "Ramón", "Mario", "Antonio", "Eduardo", "Javier", "Ricardo", "Federico", "Honorato", "Gumersindo", "Atanasio", "Hipólito", "Salvador", "Luis", "Rubén", "Héctor", "Julio", "Rangel", "Pierre"]
lista_apellidos = ["Castellanos", "Castañeda", "Aragón", "Hernández", "Márquez", "Vázquez", "Velázquez", "Solís", "Alvarado", "Valencia", "Molina", "Leana", "Goicochea", "López", "Foucalt", "Pérez", "Prado"]

indice_nombre = random.randint (0, len (lista_nombres)-1)
indice_apellidos = random.randint (0, len (lista_apellidos)-1)

nombre = lista_nombres [indice_nombre]
apellido = lista_apellidos [indice_apellidos]

print ("{0} {1}".format (nombre, apellido))
