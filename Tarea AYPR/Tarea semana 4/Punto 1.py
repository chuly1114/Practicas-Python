# Pares e impares
import os

os.system("cls")

numero = int(input("Introduzca la cantidad de números que deseea evaluar: "))

acumulador_par = 0
acumulador_impar = 0
for n in range(numero):
    z = int(input("Ingrese el número: "))
    if z == 0:
        continue
    elif z % 2 == 0:
        acumulador_par += 1
    else:
        acumulador_impar += 1

print("Pares", acumulador_par)
print("Impares", acumulador_impar)
