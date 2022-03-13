#Programa escala numerica
def fun_menor(a):
    """Encuentra menor valor en arreglo a
    (list)-> int
    """
    menor = a[0]
    for i in range(1, len(a)):
        if menor >= a[i]:
            menor = a[i]
    return menor


#
def fun_mayor(a):
    """Encuentra mayor valor en arreglo a
    (list)-> int
    """
    mayor = a[0]
    for i in range(1, len(a)):
        if mayor <= a[i]:
            mayor = a[i]
    return mayor


def rescala(a):
    """Modifica valores del arreglo a
    (List 1D) -> List 1d
    """
    long = len(a)
    menor = fun_menor(a)
    mayor = fun_mayor(a)
    for i in range(long):
        a[i] = (a[i] - menor) / (mayor - menor)
    return (a)


#
def main():
    #Entrada de datos
    linea = input("? ")
    linea = linea.split(",")
    for i in range(len(linea)):
        linea[i] = float(linea[i])
    linea = rescala(linea)
    for i in range(len(linea)):
        linea[i] = round(linea[i], 1)
    print(linea)


if __name__ == "__main__":
    main()
