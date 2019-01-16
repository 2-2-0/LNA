# basic narrative exercise 2
# algorithmic narrative lab / (LNA in spanish)
# User input string substitution into a straight paragraph
# by 220 & AA (2019) GPLv3 license

nombre = input ("¿Cómo te llamas? ")
objeto = input ("Nombre de un objeto raro: ")
color = input ("¿Tu color favorito? ")
animal = input ("Algún animal exótico: ")

narrativa = "{0} salió de su casa para buscar un {1} de color {2} para que le quedara a su {3}".format (nombre, objeto, color, animal)

print (narrativa)
