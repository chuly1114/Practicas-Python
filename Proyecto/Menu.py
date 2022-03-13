import os

os.system("cls")


def main():
    deportistas = []
    edades = []
    estaturas = []
    camisetas = deportistas[:]
    edad = 0
    estatura = 0
    numero_deportistas = int(input("Diga el numero de deportistas: "))
    for i in range(numero_deportistas):
        nombre = input("Diga el nombre del deportista " + str(i + 1) + " : ")
        estatura = input("Diga la estatura del deportista " + str(i + 1) + " : ")
        edad = input("Diga la edad del deportista " + str(i + 1) + " : ")
        deportistas.append(nombre)
        estaturas.append(estatura)
        edades.append(edad)
        camisetas.append(i + 1)
    """print("1. Cuantos deportistas tienen una edad determinada.")
    print("2. Hallar si un estudiante especifico se encuentra registrado.")
    print("3. Hallar la posición en la que se encuentra un deportista.")
    print("4. Hallar la posición en la que se encuentra un deportista con una inicial determinada")
    print("5. Edad promedio de los deportistas.")
    print("6. Estatura promedio de los deportistas.")
    print("7. Hallar el deportista de menor edad.")
    print("8. Hallar el deportista de mayor edad.")
    print("9. Hallar el deportista de menor estatura.")
    print("10. Hallar el deportista de mayor estatura.")
    print("11. Saber cuál es el nombre que más se repite.")
    print("12. Eliminar un estudiante del registro.")
    print("13. Ordenar los estudiantes alfabeticamente.")
    print("14. Ordenar los estudiantes por edad, de menor a mayor.")
    print("15. Ordenar los estudiantes por estatura, de mayor a menor.")
    print("16. Generar un equipo con los etudiantes de edad par.")
    print("17. Generar un equipo con estudiantes con la misma inicial.") 
    print("18. Generar un equipo con los estudiantes cuya edad se encuentre en un rango especifico.")
    print("19. Añadir un deportista.")
    print("20. Salir del menú.")
    dato = int(input("¿Qué dato desea saber?: "))"""


main()
