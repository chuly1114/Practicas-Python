import os

os.system("cls")

posicion_inicial1 = int(input("Ingrese la posicion x del robot: "))
posicion_inicial2 = int(input("Ingrese la posicion y del robot: "))
cambio = input("Ingrese la direccion hacia donde quiere mover el robot: ")

if cambio == "up":
    posicion_inicial2 += 1
elif cambio == "ne":
    posicion_inicial1 += 1
    posicion_inicial2 += 1
elif cambio == "right":
    posicion_inicial1 += 1
elif cambio == "se":
    posicion_inicial1 += 1
    posicion_inicial2 -= 1
elif cambio == "down":
    posicion_inicial2 -= 1
elif cambio == "so":
    posicion_inicial1 -= 1
    posicion_inicial2 -= 1
elif cambio == "left":
    posicion_inicial1 -= 1
elif cambio == "no":
    posicion_inicial1 -= 1
    posicion_inicial2 += 1
else:
    print("No introdujo un comando valido.")

print("La nueva posicion del robot es: [", posicion_inicial1, ",", posicion_inicial2, "]")
# vector = [posicion_inicial1, posicion_inicial2]
# for i in vector:
#     print(i)
# print(vector)