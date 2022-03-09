import os

os.system("cls")

limite_dias = 30
peso_inicial1 = int(input("Ingrese el peso inicial del perro 1: "))
peso_inicial2 = int(input("Ingrese el peso inicial del perro 2: "))

peso1 = 0
peso2 = 0

for n in range(limite_dias):
    print("Dia", n + 1, ": ")
    peso1 = int(input("    Ingrese el peso del perro 1: "))
    peso2 = int(input("    Ingrese el peso del perro 2: "))
    if peso1 == peso2:
        print("Los pesos de los 2 perros fueron iguales")
    elif peso1 > peso2:
        print("El peso del perro 1 fue mayor que el peso del perro 2")
    else:
        print("El peso del perro 2 fue mayor que el peso del perro 1")

diferencia1 = peso1 - peso_inicial1
diferencia2 = peso2 - peso_inicial2

if diferencia1 == diferencia2:
    print("Los perros terminaron pesando lo mismo")
elif diferencia2 > diferencia1:
    print("El perro 2 gano mas peso que el perro 1")
else:
    print("El perro 1 gano mas peso que el perro 2")
