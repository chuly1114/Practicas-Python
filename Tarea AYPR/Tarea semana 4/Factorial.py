import os

os.system("cls")

f = (int(input("Ingrese el número al que desea hallarle el factorial:")))
fac = 1

while f > 0:
    fac *= f
    f -= 1
print(fac)