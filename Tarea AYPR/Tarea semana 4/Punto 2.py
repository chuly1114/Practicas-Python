#Mario el saltador de bolardos

import os

os.system("cls")


def main():
    saltos_arriba = 0
    saltos_abajo = 0
    anterior_bolardo = 0
    siguiente_bolardo = None

    while siguiente_bolardo != 0:
        siguiente_bolardo = int(input("Introduzca la altura del bolardo: "))
        if siguiente_bolardo > anterior_bolardo:
            saltos_arriba += 1
        elif siguiente_bolardo < anterior_bolardo:
            saltos_abajo += 1
        anterior_bolardo = siguiente_bolardo

    print("Saltos arriba:", saltos_arriba)
    print("Saltos abajo:", saltos_abajo)


main()