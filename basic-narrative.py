# basic narrative exercise
# algorithmic narrative lab / (LNA in spanish)
# Variable random mixing into a straight paragraph
# by 220 & AA (2019) GPLv3 license

import random

lista_senoras = ["Lupita", "Mary", "Swagert", "Donovan", "Tere", "Chayo", "Conchita"]
lista_locaciones = ["teatro", "mercado", "supermercado", "cine", "atrio", "barrio", "cementerio", "panteón"]
lista_compras = ["pinole", "camote", "cera", "huesos", "cuerpos", "ojos", "rutabagah"]
lista_personas = ["vendedor", "sepulturero", "mico", "perro", "gato", "cuervo", "tendero"]

lista_ofensas = ["inútil", "lamesobres", "montatapias", "animal", "imbécil"]

indice_senora = random.randint (0, len (lista_senoras)-1)
indice_locacion = random.randint (0, len (lista_locaciones)-1)
indice_compra = random.randint (0, len (lista_compras)-1)
indice_persona = random.randint (0, len (lista_personas)-1)
indice_ofensa = random.randint (0, len (lista_ofensas)-1)

senora = lista_senoras [indice_senora]
locacion = lista_locaciones [indice_locacion]
compra = lista_compras [indice_compra]
persona = lista_personas [indice_persona]
ofensa = lista_ofensas [indice_ofensa]

narrativa = "La señora {0} salió al {1} a comprar {2}. Se acercó a un {3} y le dirigió la palabra...\n\n'{4}', le exclamó.".format (senora, locacion, compra, persona, ofensa)

print (narrativa)
