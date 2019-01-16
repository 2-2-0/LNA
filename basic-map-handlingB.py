# basic map handling
# algorithmic narrative lab / (LNA in spanish)
# Text adventure mechanism
# by 220 & AA (2019) GPLv3 license

mapa = [
    ("caverna", None, 2, None, None, "Hay unos esclavos aquí"),
    ("entrada", None, None, 2, None, "Estás en la entrada"),
    ("hoguera", 0, None, None, 1, "Una hoguera calientita")
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
