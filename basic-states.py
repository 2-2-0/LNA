# basic states handling
# algorithmic narrative lab / (LNA in spanish)
# Text adventure mechanism
# by 220 & AA (2019) GPLv3 license

descripcion_cuarto = "Hay una cómoda cama en medio del cuarto, al lado, una cómoda con uno de los cajones abiertos..."

foco_prendido = False
lampara_celular = False

while True:
    if (foco_prendido==True or lampara_celular==True):
        print (descripcion_cuarto)
    accion = input ('(f/l): ')

    if (accion=='f'):
        foco_prendido = not foco_prendido
    if (accion=='l'):
        lampara_celular = not lampara_celular
