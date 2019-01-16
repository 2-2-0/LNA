# basic map handling
# algorithmic narrative lab / (LNA in spanish)
# Text adventure mechanism
# by 220 & AA (2019) GPLv3 license

mapa = [
    ("estudio", None, 2, None, None, "Estás en un estudio pequeño donde se encuentra una mesa con un libro"),
    ("recámara", None, 4, 2, None, "La recámara es pequeña pero tiene un cómodo catre"),
    ("sala", 0, 5, 3, 1, "La sala es acogedora pero oscura"),
    ("entrada", None, None, None, 2, "Hay una puerta frente a ti"),
    ("baño", 1, None, 5, None, "El baño está sucio y frio"),
    ("comedor", 2, None, 6, 4, "El comedor está vacío"),
    ("cocina", None, None, None, 5, "Hay muchas cucarachas en la cocina")
]

ubicacion = 1

def describeLocacion ():
    global ubicacion

    cuarto = mapa [ubicacion]
    desc = cuarto [5]

    print (desc)

def cambiarLocacion (direccion):
    global ubicacion

    cuarto = mapa [ubicacion]
    siguiente_destino = None

    if direccion=='n':
        siguiente_destino = cuarto [1]

    if direccion=='s':
        siguiente_destino = cuarto [2]

    if direccion=='e':
        siguiente_destino = cuarto [3]

    if direccion=='o':
        siguiente_destino = cuarto [4]

    if (siguiente_destino==None):
        print ("Bump!")
    else:
        ubicacion = siguiente_destino


while True:
    describeLocacion ()
    eleccion = input ("(n/s/e/o): ")
    cambiarLocacion (eleccion)
