import os

os.system("cls")


class Deportista:

    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre

    def __str__(self):
        return "El nombre es: " + self.nombre + str(self.edad)


def main():
    deportistas = []

    for i in range(1):
        nombre = input("Digite el nombre del deportista " + str(i + 1) + ": ")
        edad = input("Digite la edad del deportista " + str(i + 1) + ": ")
        deportistas += [Deportista(nombre, edad)]
    print(deportistas[0])


main()
