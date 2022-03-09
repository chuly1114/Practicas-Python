edad = int(input("¿Cuantos años tiene?:"))
if edad >= 18:
    print("Usted es mayor de edad.")
elif edad >= 0 and edad < 18:
    print("Usted no es mayor de edad.")
else:
    print("Usted no ha nacido.")
